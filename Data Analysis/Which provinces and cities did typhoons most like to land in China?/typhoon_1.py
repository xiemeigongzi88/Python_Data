# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 01:04:34 2019

@author: sxw17
"""

from bs4 import BeautifulSoup
import requests

import pandas as pd 
from selenium import webdriver
from lxml import etree

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\DATA\\EDA')

url='http://www.stwc.icoc.cc/h-col-205.html'

driver = webdriver.Chrome()
driver.get(url)

table = driver.find_element_by_xpath("//div[@class='formMiddleContent formMiddleContent1825']")


table = etree.tostring(table, encoding='utf-8').decode()


response = requests.get(url)

'''
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36


Cookie: _cliid=hqAvoSiL6MriejL4; _ga=GA1.2.2085156481.1568354960; _gid=GA1.2.695197334.1568354960; _siteStatId=c29ceebf-24f1-43fa-aaef-1dc44f02eeb5; _siteStatDay=20190913; _siteStatRedirectUv=redirectUv_5322329; _siteStatVisitorType=visitorType_5322329; _siteStatVisit=visit_5322329; _siteStatVisitTime=1568354960930; _checkSiteLvBrowser=true

'''

url='http://www.stwc.icoc.cc/h-col-205.html'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

response = requests.get(url, headers=headers)

table=pd.read_html(response.text, encoding='utf-8')

#df = pd.DataFrame(table)
# table 14 16 17 
# 19 20 
# 21  22  23  24 25  26  28

# 22  24  26  28 

#df.to_csv('typhoon.csv')

df1 = pd.DataFrame(table[22])
df2 = pd.DataFrame(table[24])
df3 = pd.DataFrame(table[26])
df4 = pd.DataFrame(table[28])


frames = [df1, df2, df3, df4]

data = pd.concat(frames)


data.columns=['CMA Number', 'Chinese Name', 'English Name', 
              'Landing Location', 'Landing Time', 'Peak Strength','Landing Strength']



#data.columns=data.iloc[0,:]


#test =pd.DataFrame({'1':[1,2,3],'2':[4,5,6], '3':[7,8,9]})


#data.rename(columns={data.columns[0]: "Number" }, inplace=True)

data.drop(index=[0], inplace=True)


from urllib import parse
from urllib.request import urlopen
import json


def get_coor(address):
    # 需填入自己申请应用后生成的ak
    ak = 'AIzaSyAi56fjVkGLV0QIMGdsIyEkpLF8YS5zgc4'
    url = 'https://maps.google.com/maps/api/geocode/json?address='
    output = 'json'
    add = parse.quote(address)  # 本文城市变量为中文，为防止乱码，先用quote进行编码
    url2 = url + add + '&output=' + output + "&ak=" + ak
    req = urlopen(url2)
    response = req.read().decode()
    #将返回的数据转化成json格式
    responseJson = json.loads(response)
    # 获取经纬度
    lon = responseJson.get('result')['location']['lng']
    lat = responseJson.get('result')['location']['lat']
    return (lat,lon)

'''
Index(['CMA Number', 'Chinese Name', 'English Name', 'Landing Location',
       'Landing Time', 'Peak Strength', 'Landing Strength'],
      dtype='object')

'''

data['coor'] = data['Landing Location'].apply(lambda x:get_coor(x))
data['lat'] = data['coor'].apply(lambda x: list(x)[0])
data['lon'] = data['coor'].apply(lambda x: list(x)[1])


key = 'AIzaSyAi56fjVkGLV0QIMGdsIyEkpLF8YS5zgc4'
url = 'https://maps.google.com/maps/api/geocode/json?address='
output = 'json'
add = parse.quote('Urumqi')  # 本文城市变量为中文，为防止乱码，先用quote进行编码
url2 = url + add + '&output=' + output + "&ak=" + key
req = urlopen(url2)
response = req.read().decode()



'''
https://maps.googleapis.com/maps/api/geocode/json?address=
1600+Amphitheatre+Parkway,+Mountain+View,
+CA&key=YOUR_API_KEY
'''

key = 'AIzaSyAi56fjVkGLV0QIMGdsIyEkpLF8YS5zgc4'
#address ='urumqi'
url = 'https://maps.googleapis.com/maps/api/geocode/json?address='

output = 'json'
add = parse.quote('乌鲁木齐')  # 本文城市变量为中文，为防止乱码，先用quote进行编码
url2 = url + add + '+CA&key='+key
req = urlopen(url2)
response = req.read().decode()

responseJson = json.loads(response)
# 获取经纬度

result_geometry = responseJson.get('results')[0]['geometry']
location = result_geometry['location']
lon = location['lng']
lat = location['lat']



def get_coor(address):
    # 需填入自己申请应用后生成的ak
    key = 'AIzaSyAi56fjVkGLV0QIMGdsIyEkpLF8YS5zgc4'
    #address ='urumqi'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    output = 'json'
    add = parse.quote(address)  # 本文城市变量为中文，为防止乱码，先用quote进行编码
    url2 = url + add + '+CA&key='+key
    req = urlopen(url2)
    response = req.read().decode()
    responseJson = json.loads(response)
    
    result_geometry = responseJson.get('results')[0]['geometry']
    location = result_geometry['location']
    lon = location['lng']
    lat = location['lat']
    return (lat,lon)

        
data['coor'] = data['Landing Location'].apply(lambda x:get_coor(x))

data['lat'] = data['coor'].apply(lambda x: list(x)[0])
data['lon'] = data['coor'].apply(lambda x: list(x)[1]) 

data.reset_index()

data.index =range(len(data))



data.to_csv('typhoon.csv', encoding="utf_8_sig")

df = pd.read_csv('typhoon.csv')


# =========================================================================

key = 'AIzaSyAi56fjVkGLV0QIMGdsIyEkpLF8YS5zgc4'
#address ='urumqi'
url = 'https://maps.googleapis.com/maps/api/geocode/json?address='

output = 'json'
add = parse.quote('广东省江门市台山市赤溪镇')  # 本文城市变量为中文，为防止乱码，先用quote进行编码
url2 = url + add + '+CA&key='+key
req = urlopen(url2)
response = req.read().decode()

responseJson = json.loads(response)
# 获取经纬度

result_geometry = responseJson.get('results')[0]['geometry']
location = result_geometry['location']
lon = location['lng']
lat = location['lat']


location_list = data['Landing Location'].tolist()

def get_coor(location_list):
    # 需填入自己申请应用后生成的ak
    key = 'AIzaSyAi56fjVkGLV0QIMGdsIyEkpLF8YS5zgc4'
    #address ='urumqi'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    output = 'json'
    
    detail=[]
    
    error_location=[]
    for i, loc in enumerate(location_list):
        try:
            add = parse.quote(loc)  # 本文城市变量为中文，为防止乱码，先用quote进行编码
            url2 = url + add + '+CA&key='+key
            req = urlopen(url2)
            response = req.read().decode()
            responseJson = json.loads(response)
            
            result_geometry = responseJson.get('results')[0]['geometry']
            location = result_geometry['location']
            lon = location['lng']
            lat = location['lat']
            
            detail.append((lat, lon))
        except Exception as e:
            print(str(e) +' '+str(i)+' '+ loc)
            error_location.append(str(i)+'-'+ loc)
            
    return detail


coordinates = get_coor(location_list)

modified_data = data.drop(index=[15])

modified_data.index=range(len(modified_data))

lat_coor = []
for location in coordinates:
    print(location[0])
    lat_coor.append(location[0])
    

lon_coor = []
for location in coordinates:
    print(location[1])
    lon_coor.append(location[1])
    
modified_data['coordinate'] = coordinates

modified_data['lat']=lat_coor
modified_data['lon']=lon_coor

# 地理逆编码，通过经纬度获取省、市、县区三级单位

def get_address(lon,lat):
    # 输入你的秘钥，获取地址http://lbsyun.baidu.com/apiconsole/key/create
    your_ak = 'mcH6sBNaAfsbkSndFI5zO90j9wUpRMFy1'
    url = 'http://api.map.baidu.com/geocoder/v2/?callback='+
    'renderReverse&extensions_town=true&location={},+
    '{}&output=json&pois=1&latest_admin=1&ak={}'.format(lat,lon,your_ak)
    
    rp = request.urlopen(url).read().decode('utf-8')
    rp = re.findall(r"\((.*)\)",rp)[0]
    rpjson= json.loads(rp)
    # 省份
    province = rpjson['result']['addressComponent']['province']
    # 城市
    city = rpjson['result']['addressComponent']['city']
    # 区县
    district = rpjson['result']['addressComponent']['district']
    data = (province, city, district)
    return data

# helpful info 
# https://developers.google.com/maps/documentation/geocoding/intro
# url ='https://maps.googleapis.com/maps/api/geocode/json?
# latlng=40.714224,-73.961452&key=YOUR_API_KEY'

key = 'AIzaSyAi56fjVkGLV0QIMGdsIyEkpLF8YS5zgc4'


for tup in coordinates[:30]:
    target=''
    target+= str(tup[0])+',-'+str(tup[1])
    print(target)
    
import requests
    
url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+'40.714224,-73.961452'+'&key='+key

response = requests.get(url)

#rp = request.urlopen(url).read().decode('utf-8')
rp = re.findall(r"\((.*)\)",rp)[0]
rpjson= json.loads(rp)
# 省份
province = rpjson['result']['addressComponent']['province']
# 城市
city = rpjson['result']['addressComponent']['city']
# 区县
district = rpjson['result']['addressComponent']['district']
data = (province, city, district)
return data

####################################3

url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+'21.975801,112.899795'+'&key='+key

req = urlopen(url)
response = req.read().decode()
responseJson = json.loads(response)
            
result = responseJson.get('results')[1]['address_components']
city = result[3]['long_name']
prinvince = result[4]['long_name']

def get_address(cor_list):
    # 输入你的秘钥，获取地址http://lbsyun.baidu.com/apiconsole/key/create
    key = 'AIzaSyAi56fjVkGLV0QIMGdsIyEkpLF8YS5zgc4'
    
    data =[]
    for i, tup in enumerate(cor_list):
        #target = ''
        target = str(tup[0])+', '+str(tup[1])
    
        try:
            url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
        
            req = requests.get(url)
            response = req.text
            responseJson = json.loads(response)
            
            result = responseJson.get('results')[1]['address_components']
            
            
            city = result[3]['long_name']
            prinvince = result[4]['long_name']
            
            '''
            elif len(result)==4:
                
                city = result[2]['long_name']
                prinvince = result[3]['long_name']
                
                '''
            data.append((prinvince, city))
        except Exception as e:
            print(str(e)+' '+str(i)+' '+ target)
            
    return data

area = get_address(coordinates)

del modified_data['area']
modified_data['area']=area


modified_data['prinvince']=area






        
# data.to_csv('typhoon.csv', encoding="utf_8_sig")
modified_data.to_csv('modified_data.csv', encoding="utf_8_sig")
        
######################
url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key
from urllib.request import urlopen

response = requests.get(url)
responseJson=json.loads(response.text)


req = urlopen(url)
response = req.read().decode('utf-8')
responseJson = json.loads(response)



url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key

req = urlopen(url)
response = req.read().decode()
responseJson = json.loads(response)

result = responseJson.get('results')[0]['address_components']

city = result[3]['long_name']
prinvince = result[4]['long_name']

data.append((prinvince, city))


# target = str(coordinates[0][0])+ ', '+str(coordinates[0][1])  # result =7 3 4 

target = '26.08539, 119.583599'  #len(result)=4 
url='https://maps.googleapis.com/maps/api/geocode/json?latlng='+target+'&key='+key       
req = requests.get(url)
response = req.text
responseJson = json.loads(response)

result = responseJson.get('results')[1]['address_components']
if len(result)==4:
    city = result[2]['long_name']
    prinvince = result[3]['long_name']

#
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    