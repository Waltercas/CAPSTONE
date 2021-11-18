import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
diamonddf = pd.read_csv('diamonds.csv')
df = diamonddf.drop('Unnamed: 0', 1)
is_numeric = None


#Function to create bar plot for non numerical characteristics
def price_nonum_characteristic(column, sample_size, max_price):
    df = diamonddf.sample(frac = sample_size)
    df = df[df['price'] <= max_price]
    df2 = df.groupby(column).mean()
    df2.plot.bar(y='price', figsize=(6,6),title=('Diamond {} VS Diamond Price'.format(column.capitalize())), xlabel=column.capitalize(), ylabel='Price')
    return plt.show()

##Function to create plot for numerical characteristics
def price_num_characteristic(column, sample_size, max_price):
    df = diamonddf.sample(frac = sample_size)
    df = df[df['price'] <= max_price]
    df2 = df.groupby(column).mean()
    df2.plot(y='price', figsize=(6,6),title=('Diamond {} VS Diamond Price'.format(column.capitalize())), xlabel=column.capitalize(), ylabel='Price')
    return plt.show()