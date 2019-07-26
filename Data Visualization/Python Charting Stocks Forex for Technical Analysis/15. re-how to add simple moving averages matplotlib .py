# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 08:10:47 2019

@author: sxw17
"""

# 15. re-how to add simple moving averages matplotlib 
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

pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web 
import datetime 

import mpl_finance as mpf
from matplotlib.dates import date2num 
#matplotlib.rcParams.update({'font.size':9})



def movingAverage(values, window):
    weights= np.repeat(1.0, window)/window
    smas=np.convolve(values, weights, 'valid')
    return smas 


def get_stock_price(stock):
    start = dt.datetime(2016,7,24)
    end = dt.datetime(2019,7,24)


    df = web.DataReader(stock,'yahoo',start, end)
    return df 

df=get_stock_price('AAPL')

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

parse_data=get_quotes(df)

def graphData(df, MA1, MA2):
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
        
        closep = data['Close']
        
        
        x=0 
        y=len(date)
        ohlc=[]
        
        
        while x<y:
            append_me=data['Date'][x], data['Open'][x], data['High'][x], data['Low'][x], data['Close'][x], data['Adj Close'][x], data['Volume'][x]
            
            ohlc.append(append_me)
            x+=1
            
        Av1=movingAverage(closep, MA1)
        Av2=movingAverage(closep, MA2)
        
        SP=len(date[MA2-1:])

        fig=plt.figure(facecolor='#07000d')
        ax1=plt.subplot2grid((7,5),(0,0), rowspan=5, colspan=5) # (2,3)
       # ax1 = plt.axes(axisbg='#07000d')
        ax1.patch.set_facecolor("#07000d")            #设置ax1区域背景颜色               
        ax1.patch.set_alpha(0.5) 
        #colorup='#77d879',colordown='#db3f3f'
        mpf.candlestick_ohlc(ax1,ohlc,width=0.4,colorup='#77d879',colordown='#db3f3f')
        
        ax1.plot(time[-SP:], Av1[-SP:])
        ax1.plot(time[-SP:], Av2[-SP:])
        
                                     
        ax1.yaxis.label.set_color('w')
        ax1.spines['bottom'].set_color('#5998ff')
        ax1.spines['top'].set_color('#5998ff')
        ax1.spines['right'].set_color('#5998ff')
        ax1.spines['left'].set_color('#5998ff')      
        plt.ylabel('Stick Price')
        ax1.grid(True, linestyle ='dotted',color='w')
        ax1.tick_params(axis='y', colors='w')
              
        #---------------------------------------------------------
        VolumeMin=volume.min()
        
        ax2=plt.subplot2grid((7,5),(5,0), rowspan=2, colspan=5)
       # ax2 = plt.axes(axisbg='#07000d')
        ax2.patch.set_facecolor("#07000d")            #设置ax1区域背景颜色               
        ax2.patch.set_alpha(0.5) 
        
        ax2.plot( time ,volume,color='#00ffe8', linewidth= 0.8)
        ax2.fill_between(time, VolumeMin, volume, facecolor='#00ffe8', alpha = 0.5)
        ax2.axes.yaxis.set_ticklabels([])
        ax2.grid(False)
        ax2.spines['bottom'].set_color('#5998ff')
        ax2.spines['top'].set_color('#5998ff')
        ax2.spines['right'].set_color('#5998ff')
        ax2.spines['left'].set_color('#5998ff') 
        ax2.tick_params(axis='x', colors='w')
        ax2.tick_params(axis='y', colors='w')
        
        ax2.yaxis.label.set_color('w')
        plt.ylabel('Stick Price')
        plt.ylabel('Volume')
        
        ax2.xaxis.set_major_locator(mticker.MaxNLocator(15))
        ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        
        
        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)

        plt.ylabel('Volume', color='w')
        '''
        for label in ax2.xaxis.get_ticklabels():
            label.set_rotation(45)
           ''' 
           
        plt.subplots_adjust(left=0.09, bottom=0.14, top=0.9, right=0.94,
                            wspace=0.2, hspace=0.07)
        
        plt.xlabel('Time')
        
        plt.suptitle('EBAY Stock Price', fontsize=20 , fontweight='bold', color='w')
        #fig.suptitle(stock+ " Stock Price")
        
        plt.setp(ax1.get_xticklabels(), visible=False)
        
        plt.show()
    except Exception as e:
        print('failed performing...', str(e))
        
graphData(parse_data, 12, 26)