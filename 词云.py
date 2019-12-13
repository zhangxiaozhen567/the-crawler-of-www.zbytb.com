import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import openpyxl 

#读取的代码：
wb = openpyxl.load_workbook('电气.xlsx')
sheet = wb['new title']
colB=sheet['B']
data = []
for B in colB:
    data.append(B.value)
text=''.join(data)

cut = jieba.cut(text)  #text为你需要分词的字符串/句子
string = ' '.join(cut)
print(len(string))
stopword=['电气','项目','有限公司','招标','公告','询价','工程','采购','改造','材料','有限责任','公司','设备']  #设置停止词，也就是你不想显示的词，这里这个词是我前期处理没处理好，你可以删掉他看看他的作用
font = r'C:\Windows\Fonts\simfang.ttf' #设置字体路径 
wc = WordCloud(font_path=font, #如果是中文必须要添加这个，否则会显示成框框
               background_color='white',
               width=1000,
               height=800,
               max_words = 200,
               stopwords = stopword
               ).generate(string)
wc.to_file('电气.png') #保存图片
plt.imshow(wc)  #用plt显示图片
plt.axis('off') #不显示坐标轴
plt.show() #显示图片