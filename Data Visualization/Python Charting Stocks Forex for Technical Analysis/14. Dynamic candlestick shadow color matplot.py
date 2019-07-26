# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 01:02:39 2019

@author: sxw17
"""

# 14. Dynamic candlestick shadow color matplot
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

parse_df=pd.read_csv('TSLA_years.csv', parse_dates=True)