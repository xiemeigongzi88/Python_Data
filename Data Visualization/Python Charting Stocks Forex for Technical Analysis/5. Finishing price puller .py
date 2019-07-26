# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:46:58 2019

@author: sxw17
"""

#5. Finishing price puller 

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python_Data\\Customizing Matplotlib Graphs and Charts\\Python Charting Stocks Forex for Technical Analysis')

import requests
import pandas as pd
import arrow
import datetime

def get_quote_data(symbol= 'AAPL', data_range='7d', data_interval='1m'):
    res = requests.get('https://query1.finance.yahoo.com/v8/finance/chart/{0}?range={1}&interval={2}'.format(symbol, data_range, data_interval))
    data = res.json()
    body = data['chart']['result'][0]
    dt = datetime.datetime
    dt = pd.Series(map(lambda x: arrow.get(x).to('EST').datetime.replace(tzinfo=None), body['timestamp']), name='Datetime')
    df = pd.DataFrame(body['indicators']['quote'][0], index=dt)
    dg = pd.DataFrame(body['timestamp'])

    return df.loc[:, ('open', 'high', 'low', 'close', 'volume')]

stocksToPull=['AAPL','GOOG','MSFT','CMG','AMZN','EBAY','TSLA']

# data = get_quote_data('AAPL', '1d', '1m')
# data.to_csv('2019_07_22_AAPL_introday data.csv')

for ticker in stocksToPull:
    data = get_quote_data(symbol=ticker)
    file_name = '2019_07_22_{0}_intraday_data.csv'.format(ticker)
    data.to_csv(file_name)
    