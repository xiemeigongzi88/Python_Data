# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 17:12:01 2019

@author: sxw17
"""

import os 
os.getcwd()
path = "C:\\Users\\sxw17\\Desktop\\DATA\\data analysis\\sexy panties in Amazon"
os.chdir(path)

import pandas as pd 

df = pd.read_csv('each_description_review.csv')

df.columns 

df['review_text']

text_list = df['review_text'].tolist()

##################################################
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
# example_sent = "This is a sample sentence, showing off the stop words filtration."
  
len(text_list)  # 2533

text =" "

for i, sen in enumerate(text_list):
    text += str(sen)
    #print(i, sen, type(sen))
    
text 

########################################
string = " "

test_list =["asdjsf fdsjnf", "fdsfhrefw  safewfv", "a ndf"]

for sen in test_list:
    string += sen
    
string

################################################


stop_words = list(stopwords.words('english')) 
add_list = ['The','the','’',',','I','\'','!','.',"n't",')','(',"'m",'...',"''","'s",'It','5']
stop_words = stop_words + add_list
  
word_tokens = word_tokenize(text) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word_tokens) 
print(filtered_sentence) 

# 统计词频
counts = {}
for i in filtered_sentence:
    counts[i] = counts.get(i,0) + 1
#print(counts)

word_counts = list(counts.items())
#print(word_counts)

word_counts.sort(key = lambda x:x[1],reverse = True)  # 按词频降序排列

# 输出结果
for i in word_counts[0:50]:
    print(i)
    
    
#############################
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, ImageColorGenerator



stopwords = {}
# isCN = 0 # 0：英文分词  1：中文分词
path = "C:\\Users\\sxw17\\Desktop\\DATA\\data analysis\\sexy panties in Amazon\\word_cloud\\"  
back_coloring_path = path + 'img.jpg'          # 设置背景图片路径
text_path = path +  'reviews.txt'               # 设置要分析的文本路径
stopwords_path = path + 'stop_word.txt'        # 停用词词表
imgname1 = path + 'WordCloudDefautColors.png'  # 保存的图片名字1(只按照背景图片形状) 
imgname2 = path + 'WordCloudColorsByImg.png'   # 保存的图片名字2(颜色按照背景图片颜色布局生成)
#font_path = r'./fonts\simkai.ttf'             # 为matplotlib设置中文字体路径  ----- 主要是中文时使用


back_coloring = imread(back_coloring_path)     # 设置背景图片 ---- back_coloring为3维数组

wc = WordCloud(font_path = None,  #font_path          # 设置字体
                background_color = 'white',    # 设置背景颜色
                max_words = 3000,              # 设置显示的最大词数
                mask = back_coloring,          # 设置背景图片
                max_font_size = 200,           # 设置字体最大值
                min_font_size = 5,             # 设置字体最小值
                random_state = 42,             # 随机有N种配色方案
                width = 1000 , height = 860 ,margin = 2 # 设置图片默认的大小，但是如果使用背景图片的话
                                                        # 那么保存的图片大小会按照其大小保存，margin为词语边缘距离
                )

#wc.generate(text) 
words = {}
for i in word_counts:
    words['{}'.format(i[0])] = i[1]
    
wc.generate_from_frequencies(words) 
# txt_freq例子为 { word1: fre1, word2: fre2,  word3: fre3,......,  wordn: fren }


plt.figure() 


# 以下代码只显示--------形状与背景图片一致，颜色为默认颜色的词云 
plt.imshow(wc) 
plt.axis("off") 
plt.show()             # 绘制词云 
wc.to_file(imgname1)   # 保存图片




# 以下代码显示--------形状与背景图片一致，颜色也与背景图颜色一致的词云 
image_colors = ImageColorGenerator(back_coloring)      # 从背景图片生成颜色值 
plt.imshow(wc.recolor(color_func=image_colors)) 
plt.axis("off") 
plt.show() 
wc.to_file( imgname2) 




# 显示原图片 
plt.figure()
plt.imshow(back_coloring, cmap=plt.cm.gray) 
plt.axis("off") 
plt.show() # 保存图片

########################################

path_img ="C:\\Users\\sxw17\\Desktop\\DATA\\data analysis\\sexy panties in Amazon\\word_cloud\\love.jpg"
bg_pic = imread(path_img)


wordcloud = WordCloud(mask=bg_pic, background_color='black', scale=10).generate(text)

image_colors = ImageColorGenerator(bg_pic)

plt.imshow(wordcloud)
plt.axis('off')
plt.show()





















