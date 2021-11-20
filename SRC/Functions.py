import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
diamonddf = pd.read_csv('diamonds.csv')

def prep_df(input_df,sample_size, max_price):
    global df
    df = input_df.drop('Unnamed: 0', 1)
    df= df.sample(frac = sample_size)
    df = df[df['price'] <= max_price]  
    return df

def price_nonum_characteristic(column):
    df2= df.sort_values(['price'], ascending=False).groupby(column).mean()
    x= df2.index
    y=df2['price']
    plt.figure(figsize=(8, 8))
    plt.bar(x, y)
    plt.title('Diamond {} Vs Diamond Average Price'.format(column.capitalize()))
    plt.xlabel('Carats')
    plt.ylabel('Price')
    return plt.show()

##Function to create plot for numerical characteristics
def price_num_characteristic(column):
    df2 = df.sort_values(['price'], ascending=False).groupby(column).mean()
    x= df2.index
    y=df2['price']
    plt.figure(figsize=(8, 8))
    plt.plot(x, y)
    plt.title('Diamond {} Vs Diamond Average Price'.format(column.capitalize()))
    plt.xlabel('Carats')
    plt.ylabel('Price')
    return plt.show()

def percentage_carat_sold(max_carat, min_carat):
    diamonds_srt_carat = df.loc[(df['carat'] >= min_carat) & (df['carat'] <= min_carat)]
    index = diamonds_srt_carat.index
    num_of_entries = len(index)
    whole_index = df.index
    num_of_all_entries= len(whole_index)
    pct_of_whole = num_of_entries/ num_of_all_entries *100
    return num_of_all_entries, num_of_entries, pct_of_whole


def carat_price(max_carat, min_carat):
    diamonds_srt_carat = df.loc[(df['carat'] >= min_carat) & (df['carat'] <= max_carat)]
    diamonds_srt_carat = diamonds_srt_carat.sort_values(['price'], ascending=False).groupby('carat').mean()
    x= diamonds_srt_carat.index
    y= diamonds_srt_carat['price']
    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.title('Diamond Carat Vs Diamond Average Price')
    plt.xlabel('Carats')
    plt.ylabel('Price')
    plt.xticks(np.arange(min(x), max(x)+0.1, 0.1))
    plt.yticks(np.arange(0, max(y)+1, 500))
    return plt.show()