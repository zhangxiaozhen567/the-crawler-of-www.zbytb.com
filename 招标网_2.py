import requests,csv,random,time,openpyxl,json,gevent
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gevent import monkey
monkey.patch_all()
from gevent.queue import Queue



# chrome_options = Options() # 实例化Option对象
# chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
# # chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"')
# driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行


work = Queue()

kw = []
#输入关键字和想要打印的页数
while 1:
    word = input('请输入想要查询的内容')
    choose = input('想要继续输入请按回车,否则输入n')
    kw.append(word)
    if choose=='n':
        break
page = int(input('请输入想要打印的页数'))
    
    #一个问题点：如果输入错误或者想重新输入无法修改
url_list=[]


for key in kw:
    for x in range(page):
        url = 'https://www.zbytb.com/zb/search.php?kw=%s&page=%d'%(key,x+1)
        url_list.append(url)
    
for url in url_list:
    #遍历url_list
    work.put_nowait(url)

def crawler():
    while not work.empty:
        #当work队列不是空值时，执行下列程序
        url = work.get_nowait()
        #用get_nowait（）函数可以把队列里的网址都取出
        r = requests.get(url)
        #用request.get（）函数可以抓取网址
        print(url,work.qsize(),r.status_code)

tasks_list = []
#创建任务空列表

for x in range(2):
    #相当于创建了2个爬虫
    task = gevent.spawn(crawler)
    #用gevent.spawn（）函数创建执行crawler（）函数的任务
    tasks_list.append(task)
    #往任务列表添加任务
gevent.joinall(tasks_list)
print(url_list)