# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 06:06:11 2019

@author: sxw17
"""

# 7. Basic Financial Graph 

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
        #volume = stock['volume']
        
        fig=plt.figure()
        ax1=plt.subplot(1,1,1) # (2,3)
        ax1.plot(time, openp)
        ax1.plot(time,high)
        ax1.plot(time,low)
        ax1.plot(time,close)
        #ax1.plot(time,volume)
        
        '''
        ax.xaxis.set(
    major_locator=mdates.DayLocator(),
    major_formatter=mdates.DateFormatter("\n%a"),
    minor_locator=mdates.HourLocator((0, 6, 12, 18)),
    minor_formatter=mdates.DateFormatter("%H:%M"),
)
        
        ax1.set_xlabel(time, #major_locator=mticker.MaxNLocator(10),
                     major_formatter=mdates.DateFormatter('%Y-%m-%d %H:%M:%S') )
        
        ax1.xaxis.set_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
        '''
        
        # 设置主刻度标签的位置,标签文本的格式
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(8))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        
        
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)


                
        plt.show()
    except Exception as e:
        print('failed performing...', str(e))
        
for stock in eachStock:
    graphData(stock)
   # time.sleep(10)




###########################################################
stock="AAPL"
stockFile='one_day_{0}'.format(stock)+'_intraday_data.csv'
print(stockFile)

stock=pd.read_csv(stockFile, parse_dates=True)

print(stock.columns)


fig=plt.figure()
ax1=plt.subplot(1,1,1) # (2,3)

time_format = '%Y-%m-%d %H:%M:%S'
time = [datetime.datetime.strptime(i, time_format) for i in stock['Datetime']]
openp= stock['open']
high= stock['high']
low= stock['low']
close = stock['close']



ax1.plot(time, openp)
ax1.plot(time,high)
ax1.plot(time,low)
ax1.plot(time,close)
ax1.grid(True)
plt.show()

'''
ax = plt.subplot('111')
plt.xlabel('X Axis', axes=ax)
plt.ylabel('Y Axis', axes=ax)
'''

ax1.xaxis.set_locator(mticker.MaxNLocator(10))
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))



