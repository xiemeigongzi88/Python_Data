# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:14:12 2019

@author: sxw17
"""

# 2. How to get free stock prices 

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python_Data\\Customizing Matplotlib Graphs and Charts\\Python Charting Stocks Forex for Technical Analysis')


import datetime as dt
import matplotlib.pyplot as plt 
from matplotlib import style 
import pandas as pd 

import fix_yahoo_finance as fy  
fy.pdr_override() 

from pandas.api.types import is_list_like

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like

import pandas_datareader.data as web 


style.use('ggplot')
start = dt.datetime(2000,1,1)
end = dt.datetime(2019,6,30)


df = web.DataReader('TSLA','yahoo',start, end)

print(df.head())

print(df.tail())
