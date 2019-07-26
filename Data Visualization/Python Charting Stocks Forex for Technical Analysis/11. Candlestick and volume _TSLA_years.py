# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 23:07:29 2019

@author: sxw17
"""

# 11. Candlestick and volume _TSLA_years

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python_Data\\Customizing Matplotlib Graphs and Charts\\Python Charting Stocks Forex for Technical Analysis')

import matplotlib.pyplot as plt

import datetime as dt
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 
import matplotlib.ticker as mticker 
from matplotlib import style 
import pandas as pd 

import fix_yahoo_finance as fy  
fy.pdr_override() 

from pandas.api.types import is_list_like

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web 
import datetime 

import pandas_datareader.data as web 
import mpl_finance as mpf
from matplotlib.dates import date2num 


# get AAPLE stock price data
def get_stock_price(stock):
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2019,7,24)


    df = web.DataReader(stock,'yahoo',start, end)
    return df 

df = get_stock_price('TSLA')


# 处理数据
def get_quotes(df):
    
    data=pd.DataFrame()
    date = df.index.tolist()
    date_str= [datetime.datetime.strftime(x, '%Y-%m-%d') for x in date ]
    data['Date']=date_str

    data['Open']= df['Open'].values
    data['High']=df['High'].values
    data['Low']=df['Low'].values
    data['Close']=df['Close'].values
    data['Adj Close']=df['Adj Close'].values
    data['Volume']=df['Volume'].values

    return data 

parse_df=get_quotes(df)



# graph it 
def graphData(df):
    try:
        
        data=pd.DataFrame()
        time_format = '%Y-%m-%d'
        date = df['Date'].tolist()
        
        time = [datetime.datetime.strptime(i, time_format) for i in date]
        volume= df['Volume']
        
        data['Date']=pd.to_datetime(date)
        data['Date']= data['Date'].apply(date2num)
    
        data['Open']= df['Open'].values
        data['High']=df['High'].values
        data['Low']=df['Low'].values
        data['Close']=df['Close'].values
        data['Adj Close']=df['Adj Close'].values
        data['Volume']=df['Volume'].values
        
        x=0 
        y=len(date)
        ohlc=[]
        
        
        while x<y:
            append_me=data['Date'][x], data['Open'][x], data['High'][x], data['Low'][x], data['Close'][x], data['Adj Close'][x], data['Volume'][x]
            
            ohlc.append(append_me)
            x+=1

        fig=plt.figure()
        ax1=plt.subplot2grid((6,5),(0,0), rowspan=4, colspan=5) # (2,3)
        
        mpf.candlestick_ohlc(ax1,ohlc,width=0.4,colorup='#77d879',colordown='#db3f3f')
        
        plt.ylabel('Stick Price')
        ax1.grid(True)
        
        
        ax2=plt.subplot2grid((6,5),(4,0), rowspan=2, colspan=5)
        ax2.bar( time ,volume, width=10, color='g')
        ax2.axes.yaxis.set_ticklabels([])
        ax2.grid(True)
        plt.ylabel('Volume')
        
        ax2.xaxis.set_major_locator(mticker.MaxNLocator(12))
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        
        
        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        plt.subplots_adjust(left=0.1, bottom=0.18, top=0.9, right=0.94,
                            wspace=0.2, hspace=0.07)
        
        plt.xlabel('Time')
        
        plt.suptitle('TSLA Stock Price', fontsize=10)
        #fig.suptitle(stock+ " Stock Price")
        
        plt.setp(ax1.get_xticklabels(), visible=False)
        
        plt.show()
    except Exception as e:
        print('failed performing...', str(e))
        
graphData(parse_df)

#######################################################################
date = parse_df['Date'].tolist()
time_format = '%Y-%m-%d'

time = [datetime.datetime.strptime(i, time_format) for i in date]
volume= parse_df['Volume']

fig=plt.figure()
plt.bar(time, volume)