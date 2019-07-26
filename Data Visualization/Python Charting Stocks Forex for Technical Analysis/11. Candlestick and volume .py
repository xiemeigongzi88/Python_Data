# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:23:43 2019

@author: sxw17
"""

# 11. Candlestick and volume 

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python_Data\\Customizing Matplotlib Graphs and Charts\\Python Charting Stocks Forex for Technical Analysis')

import time 
import datetime 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates 
from mpl_finance import candlestick2_ochl
import matplotlib
matplotlib.rcParams.update({'font.size':9})
from matplotlib.dates import date2num 
import mpl_finance as mpf

# get intraday fb stock data 
def get_quote_data(symbol= 'AAPL', data_range='1d', data_interval='1m'):
    res = requests.get('https://query1.finance.yahoo.com/v8/finance/chart/{0}?range={1}&interval={2}'.format(symbol, data_range, data_interval))
    data = res.json()
    body = data['chart']['result'][0]
    dt = datetime.datetime
    dt = pd.Series(map(lambda x: arrow.get(x).to('EST').datetime.replace(tzinfo=None), body['timestamp']), name='Datetime')
    df = pd.DataFrame(body['indicators']['quote'][0], index=dt)
    dg = pd.DataFrame(body['timestamp'])

    return df.loc[:, ('open', 'high', 'low', 'close', 'volume')]

df_FB = get_quote_data(symbol='FB') 
df_FB.to_csv('one_day_FB_intraday_data.csv')

#df= pd.read_csv('one_day_FB_intraday_data.csv', parse_dates=True)

# graph it 
def graphData(stock):
    try:
        ticker = stock
        stockFile='one_day_{0}'.format(stock)+'_intraday_data.csv'
        
        stock=pd.read_csv(stockFile, parse_dates=True)
        
        #time_format = '%Y-%m-%d %H:%M:%S'

        #time = [datetime.datetime.strptime(i, time_format) for i in stock['Datetime']]
        
       # time = time.apply(date2num)
        stock['Datetime']=pd.to_datetime(stock['Datetime'])
        stock['Datetime']=stock['Datetime'].apply(date2num)
        time=stock['Datetime']
        openp= stock['open']
        high= stock['high']
        low= stock['low']
        close = stock['close']
        volume= stock['volume']
        '''
        frame = plt.gca()
        # y 轴不可见
        frame.axes.get_yaxis().set_visible(False)
        # x 轴不可见
        frame.axes.get_xaxis().set_visible(False)
        '''
        
        x=0 
        y=len(time)
        candleAr=[]
        while x<y:
            appendLine=time[x], openp[x], high[x], low[x], close[x]
            candleAr.append(appendLine)
            x+=1 
        
        
        #candlestick2_ochl(ax1, candleAr, width=13fasdfas)
        
        fig=plt.figure()
        ax1=plt.subplot2grid((6,5),(0,0), rowspan=4, colspan=5) # (2,3)
        
        mpf.candlestick_ohlc(ax1,candleAr,width=0.4,colorup='#77d879',colordown='#db3f3f')
        
        plt.ylabel('Stick Price')
        ax1.grid(True)
        plt.title(str(ticker))
        
        ax2=plt.subplot2grid((6,5),(4,0), sharex=ax1, rowspan=2, colspan=5)
        ax2.bar(time, volume, width=0.002, color='g')
        ax2.axes.yaxis.set_ticklabels([])
        ax2.grid(True)
        plt.ylabel('Volume')
        
        ax2.xaxis.set_major_locator(mticker.MaxNLocator(12))
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        
        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        plt.subplots_adjust(left=0.1, bottom=0.18, top=0.9, right=0.94,
                            wspace=0.2, hspace=0.07)
        
        plt.xlabel('Time')
        
        plt.suptitle('2019 07 22 Stock Price', fontsize=10)
        #fig.suptitle(stock+ " Stock Price")
        
        plt.setp(ax1.get_xticklabels(), visible=False)
        
        plt.show()
        #fig.savefig('example.png')
    except Exception as e:
        print('failed performing...', str(e))
        
stock='FB'
graphData(stock)