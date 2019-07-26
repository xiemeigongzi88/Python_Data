# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 21:43:02 2019

@author: sxw17
"""

# JSON 文件存储
#读取 JSON 

import json

import os 
os.getcwd()
os.chdir('C:\\Users\\sxw17\\Desktop\\python learning\\Python_Data\\Customizing Matplotlib Graphs and Charts\\Python Charting Stocks Forex for Technical Analysis')




string = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(string))
data = json.loads(string)
print(data)
print(type(data))

data[0]
data[0]['name']

# 输出 JSON
import json 
data 

with open('data.json','w') as file:
    file.write(json.dumps(data))


# JSON 的数据需要使用双引号 不能用单引号
import json 

with open('data.json', 'r')  as file:
    content = file.read()
    data = json.loads(content)
    
    print(data)

