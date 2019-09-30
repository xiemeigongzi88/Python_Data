# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:44:54 2019

@author: sxw17
"""

from bs4 import BeautifulSoup
import requests

import pandas as pd 
from selenium import webdriver
from lxml import etree
import json
import urllib
import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\DATA\\EDA')

data =pd.read_csv('modified_data.csv')

del data['Unnamed: 0']

url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key

req = requests.get(url)
response = req.text
responseJson = json.loads(response)

result = responseJson.get('results')[0]['address_components']

city = result[3]['long_name']
prinvince = result[4]['long_name']

coordinates = data['coordinate'].tolist()

len(coordinates) == len(data)

#############################
# 4  length = 6 

target = coordinates[4].split(',')[0][1:]+', '+coordinates[4].split(',')[1][:-1]

url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
req = requests.get(url)
response = req.text
responseJson = json.loads(response)

result = responseJson.get('results')[0]['formatted_address']

city = result.split(',')[-4].strip()
prinvince = result.split(',')[-3].strip()


###################################
# 6   length = 5 最后是 China
target = coordinates[6].split(',')[0][1:]+', '+coordinates[6].split(',')[1][:-1]

url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
req = requests.get(url)
response = req.text
responseJson = json.loads(response)

result = responseJson.get('results')[0]['formatted_address']

city = result.split(',')[-3].strip()
prinvince = result.split(',')[-2].strip()


###########################################
#7  length = 5  最后是邮政编码 

target = coordinates[7].split(',')[0][1:]+', '+coordinates[7].split(',')[1][:-1]

url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
req = requests.get(url)
response = req.text
responseJson = json.loads(response)

result = responseJson.get('results')[0]['formatted_address']

for i, item in enumerate(result.split(',')):
    if 'Sheng' in item:
        prinvince = item.strip()
        city = result.split(',')[i-1].strip()
        
#city = result.split(',')[-4].strip()
#prinvince = result.split(',')[-3].strip()

###########################################
#10  length = 5 China

target = coordinates[10].split(',')[0][1:]+', '+coordinates[10].split(',')[1][:-1]

url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
req = requests.get(url)
response = req.text
responseJson = json.loads(response)

result = responseJson.get('results')[0]['formatted_address']

for i, item in enumerate(result.split(',')):
    if 'Sheng' in item:
        prinvince = item.strip()
        city = result.split(',')[i-1].strip()

#city = result.split(',')[-3].strip()
#prinvince = result.split(',')[-2].strip()



#############################################



def get_address(cor_list):

    key = 'AIzaSyAi56fjVkGLV0QIMGdsIyEkpLF8YS5zgc4'
    
    data =[]
    for i, tup in enumerate(cor_list):
        #target = ''
        target = tup.split(',')[0][1:]+', '+tup.split(',')[1][:-1]
    
        try:
            url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
        
            req = requests.get(url)
            response = req.text
            responseJson = json.loads(response)
            
            #result = responseJson.get('results')[1]['address_components']
            result = str(responseJson.get('results'))
            
            if result.split(',')[-1].strip()=='China':
                #city = result[3]['long_name']
                #prinvince = result[4]['long_name']
                city = result.split(',')[-3].strip()
                prinvince = result.split(',')[-2].strip()
                
            

            else:
                city = result.split(',')[-4].strip()
                prinvince = result.split(',')[-3].strip()
                
            data.append((prinvince, city))
        except Exception as e:
            print(str(e)+' '+str(i)+' '+ target)
            
    return data

area = get_address(coordinates)


#################################
# 15 
target = coordinates[15].split(',')[0][1:]+coordinates[15].split(',')[1][:-1]

url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
req = requests.get(url)
response = req.text
responseJson = json.loads(response)

result = str(responseJson.get('results'))

for i, item in enumerate(result.split(',')):
    if 'Sheng' in item:
        prinvince = item.strip()
        city = result.split(',')[i-1].strip()




###########################################
#10  length = 5 China

target = coordinates[10].split(',')[0][1:]+', '+coordinates[10].split(',')[1][:-1]

url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
req = requests.get(url)
response = req.text
responseJson = json.loads(response)

result = str(responseJson.get('results'))

for i, item in enumerate(result.split(',')):
    if 'Sheng' in item:
        prinvince = item.strip()
        city = result.split(',')[i-1].strip()

#city = result.split(',')[-3].strip()
#prinvince = result.split(',')[-2].strip()



#############################
# 4  length = 6 

target = coordinates[4].split(',')[0][1:]+', '+coordinates[4].split(',')[1][:-1]

url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
req = requests.get(url)
response = req.text
responseJson = json.loads(response)

result = str(responseJson.get('results'))

for i, item in enumerate(result.split(',')):
    if 'Sheng' in item:
        prinvince = item.strip()
        city = result.split(',')[i-1].strip()




def get_address(cor_list):

    key = 'AIzaSyAi56fjVkGLV0QIMGdsIyEkpLF8YS5zgc4'
    
    data =[]
    for i, tup in enumerate(cor_list):
        #target = ''
        target = tup.split(',')[0][1:]+', '+tup.split(',')[1][:-1]
    
        try:
            url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
        
            req = requests.get(url)
            response = req.text
            responseJson = json.loads(response)
            
            #result = responseJson.get('results')[1]['address_components']
            result = str(responseJson.get('results'))
            
            
            for i, item in enumerate(result.split(',')):
                if 'Sheng' in item:
                    prinvince = item.strip()
                    city = result.split(',')[i-1].strip()
                
            data.append((prinvince, city))
            
        except Exception as e:
            print(str(e)+' '+str(i)+' '+ target)
            
    return data

area = get_address(coordinates)

len(area)==len(data)


data['area']= area

city=[]
prinvince =[]

for tup in area:
    city.append(tup[1])
    prinvince.append(tup[0])
    
len(city)==len(prinvince)==len(data)

data['city']=city 
data['prinvince']= prinvince

#############################################################
from shapely.geometry import LineString,Point
import geopandas


# 使用shapely库的Point方法，将经、纬度数据转换地理几何点
xy = [Point(xy) for xy in zip(data.lon,data.lat)]
# 将data数据读取为GeoDataFrame格式，这是geopandas库用于地理空间可视化的专有数据格式
geo_data = geopandas.GeoDataFrame(data,geometry=xy)

# 读取已经下载好的中国地图shapefile格式底图
gdf = geopandas.read_file(r"bou2_4p.shp")
# 展示中国地图
ax = gdf.plot(figsize=(20, 20), alpha=0.2, edgecolor='green',color='green',linewidth=1)
# 在中国地图底图上展示台风登陆点
geo_data.plot(ax=ax,color='red',markersize=10)
plt.rc('font', family='SimHei', size=18)

plt.xlim(100, 140)
plt.ylim(15,55)

plt.grid() 
#plt.set_facecolor('aliceblue')
plt.title('1945-2015 全国沿海省份台风登陆地点分布图',size=30)
plt.show()


##############################
from wordcloud import WordCloud

# 词云展示 台风登陆的省份分布
words = ','.join(data['prinvince'].values.tolist())
wc = WordCloud(
    background_color="white", #背景颜色
    max_words=300, #显示最大词数
    font_path='./fonts/simhei.ttf',#显示中文
    min_font_size=5,
    max_font_size=100,
    width=500  #图幅宽度
    )
x = wc.generate(words)
image = x.to_image()
image




# 词云展示 台风登陆的城市分布
words = ','.join(data['city'].values.tolist())
wc = WordCloud(
    background_color="white", #背景颜色
    max_words=300, #显示最大词数
    font_path='./fonts/simhei.ttf',#显示中文
    min_font_size=5,
    max_font_size=100,
    width=500  #图幅宽度
    )
x = wc.generate(words)
image = x.to_image()
image

import re

# 新建data_1
data_1 = data[['登陆时间','登陆强度','巅峰强度','省']].dropna()
data_1['登陆等级'] = data_1['登陆强度'].apply(lambda x:int(re.match('\d+',str(x).split('，')[0]).group()))
data_1['巅峰等级'] = data_1['巅峰强度'].apply(lambda x:int(re.match('\d+',str(x).split('，')[0]).group()))
data_1['登陆年份'] = data_1['登陆时间'].apply(lambda x:x.year)
data_1['登陆月份'] = data_1['登陆时间'].apply(lambda x:x.month)




data_1= data[['Landing Time', 'Landing Strength', 'Peak Strength','prinvince']].dropna()

data_landing = []

for item in data_1['Landing Strength']:
    i = item.split('，')[0][:-1]
    if '+' in i:
       i=i[:-1]
       
    print((i))
    data_landing.append(int(i))


data_1['Landing_num']=data_landing


data_peak=[]
for item in data_1['Peak Strength']:
    i = item.split('，')[0][:-1]
    if '+' in i:
       i=i[:-1]
       
    print((i))
    data_peak.append(int(i))


data_1['peak_num']=data_peak


data_year=[]
data_month=[]

for time in data_1['Landing Time']:
    year= int(time.split('年')[0])
    month = int((time.split('年'))[1].split('月')[0])
    print(str(year) +' '+ str(month))
    data_year.append(year)
    data_month.append(month)
    
data_1['year']=data_year
data_1['month']=data_month


data_1['prinvince'].unique()

data_2=data_1.copy()
data_2['prinvince'].unique()

data_2[data_2['prinvince']=="'formatted_address': '200A Shengang Ave"]

data_2.drop(index=[23])

data_1.drop(index=[23], inplace=True)

import seaborn as sns
plt.figure(figsize=(18,10))
plt.xticks(fontsize = 20,rotation='45')

sns.swarmplot(x='prinvince',y='Landing_num',data=data_1,palette='Set1')
plt.title("1945-2015 各省台风登陆等级分类散点图（点数多少代表台风数量）",size=20)
plt.show()

####################################################

# 每年台风数量
year_counts = data_1['year'].value_counts().sort_index()
plt.figure(figsize=(15,6))
plt.plot(year_counts,lw=2)
plt.plot(year_counts,'ro',color='b')
x = year_counts.index.tolist()
y_mean = [year_counts.mean()]*year_counts.shape[0]
plt.plot(x,y_mean,'--')
plt.xlabel('年份')
plt.ylabel('次数')
plt.rc('font', family='SimHei', size=18) 
plt.title('1945-2015 全国每年台风登陆数量',size=20)
plt.show()


#############################################3

# 不同月份台风登陆时的强度等级
data_3 = data_1.groupby(['month','Landing_num'],as_index=False)['Landing Time'].count()
data_3 = data_3.rename(columns={'Landing Time':'Landing_Counts'})
# data_2.sort_values(['登陆等级','登陆月份'])
data_3_pivot = data_3.pivot('Landing_num','month','Landing_Counts')
# data_2_pivot
plt.figure(figsize=(8,6))
sns.heatmap(data_3_pivot)
plt.title('1945-2015 全国台风登陆次数热力图（按月份-登陆等级）',size=20)
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(x='month',y='Landing_num',data=data_3)
plt.title('1945-2015 全国台风登陆等级分布箱图',size=20)
plt.show()


# 不同月份台风登陆时的强度等级
data_2 = data_1.groupby(['month','peak_num'],as_index=False)['Landing Time'].count()
data_2 = data_2.rename(columns={'Landing Time':'Landing Counts'})
data_2_pivot = data_2.pivot('peak_num','month','Landing Counts')
plt.figure(figsize=(8,6))
sns.heatmap(data_2_pivot)
plt.title('1945-2015 全国台风登陆次数热力图（按月份-巅峰等级）',size=20)
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(x='month',y='peak_num',data=data_1)
plt.title('1945-2015 全国台风巅峰等级箱图',size=20)
plt.show()







































































