import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
diamonddf = pd.read_csv('../Data/diamonds.csv')


def prep_df(input_df,sample_size, max_price):
    '''This function takes a raw dataframe with all value and reduces it to a size and 
    takes the max price for a diamond that the user is working with and returns a dataframe'''
    global df
    df = input_df.drop('Unnamed: 0', 1)
    df= df.sample(frac = sample_size)
    df = df[df['price'] <= max_price]  
    return df

def price_nonum_characteristic(column):
    '''This function takes a prepped dataframe and sorts diamonds by price and returns a bar chart
    with the average price of a diamond against a non numerical or categorical characteristic inputted by user'''
    if isinstance(column, str):
        print('Please enter a non numeric column.')
    else:    
        df2= df.sort_values(['price'], ascending=False).groupby(column).mean()
        x= df2.index
        y=df2['price']
        plt.figure(figsize=(8, 8))
        plt.bar(x, y)
        plt.title('Diamond {} Vs Diamond Average Price'.format(column.capitalize()))
        plt.xlabel('Carats')
        plt.ylabel('Price')
        return plt.show()

def price_num_characteristic(column):
    '''This function takes a prepped dataframe and sorts diamonds by average price and
    returns a graph of average diamond price against a numerical characteristic input by the user'''
    if isinstance(column, str):
        print('Please enter a numeric column.')
    else:    
        df2 = df.sort_values(['price'], ascending=False).groupby(column).mean()
        x= df2.index
        y=df2['price']
        plt.figure(figsize=(8, 8))
        plt.plot(x, y)
        plt.title('Diamond {} Vs Diamond Average Price'.format(column.capitalize()))
        plt.xlabel('Carats')
        plt.ylabel('Price')
        return plt.show()

def percentage_carat_sold(max_carat, min_carat, input_df):
    '''This function takes a dataframe and returns the percentage of diamonds that are 
    in the range of the minimum and maximum number of carat inputted by the user'''
    diamonds_srt_carat = input_df.loc[(input_df['carat'] >= min_carat) & (input_df['carat'] <= max_carat)]
    index = diamonds_srt_carat.index
    num_of_entries = len(index)
    whole_index = df.index
    num_of_total_entries= len(whole_index)
    pct_of_whole = num_of_entries/ num_of_total_entries *100
    pct_of_whole=('%.2f'%pct_of_whole)
    answer = 'There are {} diamonds in the data set \n{} of them are inbetween {} and {} carat\nmaking up {} percent of the data set'.format(num_of_total_entries, num_of_entries, min_carat, max_carat, float(pct_of_whole))  
    return print(answer)


def graph_carat_price(max_carat, min_carat):
    '''This function display a graph of diamonds sorted by max and min carat
    to focus on a smaller portion'''
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