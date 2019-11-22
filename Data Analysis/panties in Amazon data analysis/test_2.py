# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:03:53 2019

@author: sxw17
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors 
# get_ipython().magic('matplotlib inline')

import os 
os.getcwd()
path = "C:\\Users\\sxw17\\Desktop\\DATA\\data analysis\\sexy panties in Amazon"
os.chdir(path)



item_info = pd.read_csv("each_description.csv")

item_info= item_info.iloc[:, 1:]

reviews = item_info.iloc[:, -1]

item_info.columns=['shop_name','product_name','total_rank','price','review_num','Read reviews that mention',
                   'shop_link','user_name','user_rank','user_short_review','Date_first_listed_on_Amazon','size','color','reviews',]

rank = item_info['total_rank'].tolist()
rank_list=[]
for each in rank:
    score = each.split()[0]
    score = float(score)
    print(score, type(score))
    rank_list.append(score)
    
item_info['rank_float'] = rank_list


# 清洗列：price
item_info['price'] = item_info['price'].str.replace('$','')
item_info['min_price'] = item_info['price'].str.split('-').str[0].astype('float')
item_info['max_price'] = item_info['price'].str.split('-').str[-1].astype('float')
item_info['mean_price'] = (item_info['max_price']+item_info['min_price'])/2

def find_na(data,cols):
    for i in cols:
            data[i].fillna(data[i].mean(),inplace = True)
    return data

item_info = find_na(item_info,['product_name', 'Read reviews that mention', 'size', 'color'])
item_info.head(5)

# 'product_name', 'Read reviews that mention', 'size', 'color'

#########################################################################
'''
['shop_name','product_name','total_rank','price','review_num','Read reviews that mention',
'shop_link','user_name','user_rank','user_short_review','Date_first_listed_on_Amazon',
'size','color','reviews',]
'''
##############################################################################
# 2、以商家维度处理数据
a = item_info.groupby('shop_name')['rank_float'].mean().sort_values(ascending=False)    # 商家星级均值
a

review_num = item_info['review_num'].tolist()
review_num_list = []
for num in review_num:
    try:
        num = float(num)
    except Exception as e:
        num = float(num.split(',')[0]+ num.split(',')[-1])
    print(num, type(num))
    review_num_list.append(num)
    
item_info['review_num'] = review_num_list


 # 商家评论数总和、均值
# b = item_info.groupby('shop_name')['reviews'].agg({'review_num':np.sum,'review_mean':np.mean})    
b = item_info.groupby('shop_name')['review_num'].agg({'review_num':np.sum,'review_mean':np.mean})
b

c = item_info.groupby('shop_name')['min_price'].mean()    # 商家最低价均值
c


d = item_info.groupby('shop_name')['max_price'].mean()    # 商家最高价均值
d

e = item_info.groupby('shop_name')['mean_price'].mean()   # 商家价格均值  
e.name = 'price_mean'
f = item_info.groupby('shop_name')['total_rank'].count()        # 商家商品数量
f.name = 'item_num'
print(a,b,c,d,e,f)

df = pd.concat([a,b,e,f],axis=1)                        # 商家商品数量百分比
df['per'] = df['item_num']/100
df['per%'] = df['per'].apply(lambda x: '%.2f%%' % (x*100))

# 标准化处理
def data_nor(df, *cols):
    for col in cols:
        colname = col + '_nor'
        df[colname] = (df[col]-df[col].min())/(df[col].max()-df[col].min()) * 10
    return df
# 创建函数，结果返回标准化取值，新列列名

df_re = data_nor(df, 'rank_float','review_mean','price_mean','item_num')
print(df_re.head(5))

############################################################
# 3、绘制图表

fig,axes = plt.subplots(4,1,figsize = (10,15))
plt.subplots_adjust(wspace =0, hspace =0.5)

# 不同商家的星级排名
df_star = df['rank_float'].sort_values(ascending = False)
df_star.plot(kind = 'bar',color = 'yellow',grid = True,alpha = 0.5,ax =axes[0],width =0.7,
                                              ylim = [3,5],title = 'Star ranking of different shops')
axes[0].axhline(df_star.mean(),label = '平均星级%.2f分' %df_star.mean() ,color = 'r' ,linestyle = '--',)
axes[0].legend(loc = 1)


# 不同商家的平均评论数排名
df_reviews_mean = df['review_mean'].sort_values(ascending = False)
df_reviews_mean.plot(kind = 'bar',color = 'blue',grid = True,alpha = 0.5,ax =axes[1],width =0.7,
                                              title = '不同商家的平均评论数排名')
axes[1].axhline(df_reviews_mean.mean(),label = '平均评论数%i条' %df_reviews_mean.mean() ,color = 'r' ,linestyle = '--',)
axes[1].legend(loc = 1)

# 不同商家的价格区间（按均价）
avg_price = (d-c)/2
avg_price.name = 'avg_price'
max_price = avg_price.copy()
max_price.name = 'max_price'

df_price = pd.concat([c,avg_price,max_price,df_re['price_mean']],axis=1)
df_price = df_price.sort_values(['price_mean'],ascending = False)
df_price.drop(['price_mean'],axis =1,inplace = True)
df_price.plot(kind = 'bar',grid = True,alpha = 0.5 , ax =axes[2],width =0.7,stacked = True,
              color= ['white','red','blue'],ylim = [0,55],title = '不同商家的价格区间')


# 不同商家的加权分排名
df_nor = pd.concat([df_re['rank_float_nor'],df_re['review_mean_nor'],df_re['price_mean_nor'],df_re['item_num_nor']],axis =1)
df_nor['nor_total'] = df_re['rank_float_nor'] + df_re['review_mean_nor'] + df_re['price_mean_nor'] + df_re['item_num_nor']
df_nor = df_nor.sort_values(['nor_total'],ascending = False)
df_nor.drop(['nor_total'],axis = 1,inplace = True)
df_nor.plot(kind = 'bar',grid = True,alpha = 0.5 , ax =axes[3],width =0.7,stacked = True,
           title = '不同商家的加权分排名')


####################################################################



# 商家数量饼图
colors = ['aliceblue','antiquewhite','beige','bisque','blanchedalmond','blue','blueviolet','brown','burlywood',
          'cadetblue','chartreuse','chocolate','coral','cornflowerblue','cornsilk','crimson','cyan','darkblue','darkcyan','darkgoldenrod',
          'darkgreen','darkkhaki','darkviolet','deeppink','deepskyblue','dimgray','dodgerblue','firebrick','floralwhite','forestgreen',
           'gainsboro','ghostwhite','gold','goldenrod']

df_per = df_re['item_num']
fig,axes = plt.subplots(1,1,figsize = (8,8))
plt.axis('equal') #保证长宽相等
plt.pie(df_per , 
        labels = df_per.index , 
        autopct = '%.2f%%',
        pctdistance = 1.05 , 
        #shadow = True ,
        startangle = 0 ,
        radius = 1.5 , 
        colors = colors,
        frame = False
        )



# 不同商家的星级/价格散点图
plt.figure(figsize=(13,8))
x = df_re['price_mean']       # x轴为均价
y = df_re['rank_float']             # y轴为星级
s = df_re['item_num']*100     # 点大小为商品数量，商品数量越大，点越大
c = df_re['review_mean']*10  # 点颜色为评论均值，评论均值越大，颜色越深红
plt.scatter(x,y,marker='.',cmap='Reds',alpha=0.8,
           s = s,c = c)
plt.grid()
plt.title('不同商家的星级/价格散点图')
plt.xlim([0,50])
plt.ylim([3,5])
plt.xlabel('price')
plt.ylabel('star')

# 绘制平均线、图例
p_mean = df_re['price_mean'].mean()
s_mean = df_re['rank_float'].mean()
plt.axvline(p_mean,label = '平均价格%.2f$' %p_mean ,color = 'r' ,linestyle = '--',)
plt.axhline(s_mean,label = '平均星级%.2f' %s_mean ,color = 'g' ,linestyle = '-.')
plt.axvspan(p_mean, 50, ymin= (s_mean-3)/(5-3), ymax=1,alpha = 0.1,color = 'g')
plt.axhspan(0, s_mean, xmin= 0 , xmax=p_mean/50,alpha = 0.1,color = 'grey')
plt.legend(loc = 2)

# 添加商家标签
for x,y,name in zip(df_re['price_mean'],df_re['rank_float'],df_re.index):
    plt.annotate(name, xy=(x,y),xytext = (0, -5), textcoords = 'offset points',ha = 'center', va = 'top',fontsize = 9)




