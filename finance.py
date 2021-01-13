#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:06:47 2021

@author: jr93714
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import bs4 as bs
import pickle
import requests

style.use('ggplot')

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    print(resp)
    soup = bs.BeautifulSoup(resp.txt)
    table = soup.find('table', {'id': 'constituents'})
    tickers = []
    for row in tavle.findAll('tr')[1:]:
          ticker = row.find('td').text
          tickers.append(ticker)
         
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)
        
    print(tickers)
    
    return tickers

save_sp500_tickers()
    



# start = dt.datetime(2000,1,1)
# end = dt.datetime(2020,12,31)

# df = web.DataReader('TSLA', 'yahoo', start, end)
# df.to_csv('tsla.csv')
# print(df.head())
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
# print(df.head())

#moving average
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#print(df.head())

#Open High Low Close
df_ohlc= df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace =True)
df_ohlc['Date']= df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values,0)

# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

