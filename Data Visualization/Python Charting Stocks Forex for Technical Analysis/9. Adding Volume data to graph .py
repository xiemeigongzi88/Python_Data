# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 13:09:29 2019

@author: sxw17
"""

# 9. Adding Volume data to graph 

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

eachStock= ['TSLA','AAPL']

def graphData(stock):
    try:
        ticker = stock
        stockFile='one_day_{0}'.format(stock)+'_intraday_data.csv'
        
        stock=pd.read_csv(stockFile, parse_dates=True)
        # data_ohlc['Date']= data_ohlc['Date'].map(mdates.date2num)
        
        # time_format = '%Y-%m-%d %H:%M'
        # time = [datetime.strptime(i, time_format) for i in mydata['timestamp']]
        time_format = '%Y-%m-%d %H:%M:%S'
        #time= stock['Datetime'].map(mdates.date2num)
        
        # datetime.datetime.strptime(date, "%Y-%m-%d")
        time = [datetime.datetime.strptime(i, time_format) for i in stock['Datetime']]
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
        
        fig=plt.figure()
        ax1=plt.subplot(2,1,1) # (2,3)
        ax1.plot(time, openp)
        ax1.plot(time,high)
        ax1.plot(time,low)
        ax1.plot(time,close)
        plt.ylabel('Stick Price')
        ax1.grid(True)
        plt.title(str(ticker))
        
        ax2=plt.subplot(2,1,2, sharex=ax1)
        ax2.bar(time, volume, width=0.002, color='g')
        ax2.grid(True)
        plt.ylabel('Volume')
        
        #ax1.plot(time,volume)
        ax2.xaxis.set_major_locator(mticker.MaxNLocator(12))
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        
        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        plt.subplots_adjust(left=0.1, bottom=0.1, top=0.9, right=0.93,
                            wspace=0.2, hspace=0.07)
        
        plt.xlabel('Time')
        #plt.ylabel('Stock Price')
        
        #sup_title= stock+"Stock Price"
        plt.suptitle('2019 07 22 Stock Price', fontsize=10)
        #fig.suptitle(stock+ " Stock Price")
        
        plt.setp(ax1.get_xticklabels(), visible=False)
        
        plt.show()
    except Exception as e:
        print('failed performing...', str(e))
        
for stock in eachStock:
    graphData(stock)
   # time.sleep(10)


#####################################################################
time = [datetime.datetime.strptime(i, time_format) for i in stock['Datetime']]
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           