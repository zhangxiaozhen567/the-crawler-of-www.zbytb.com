import requests,csv,random,time,openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



start = time.time()
chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
# chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"')
driver = webdriver.Chrome(options = chrome_options) # 设置引擎为Chrome，在后台默默运行



#定义关键字
def keywords():
    global kw,page#kw关键字的列表和定义的页数设置成全局变量
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


def get_html():
    #首先调用的是关键字的函数
    keywords()
    #接下来遍历每一个关键字
    #一个问题点：如果输入的关键字找不到会报错后面要加try函数
    for key in kw:
        data = []#这个data是把所有爬取到的数据总和加入以便后面存储
        for x in range(page):#遍历每一页
            url = 'https://www.zbytb.com/zb/search.php?kw='
            driver.get(url+'%s+&page=%d'%(key,x+1))#获取输入某个关键字和页面
            time.sleep(1)
            sp = spider()#调用spider函数并把返回值给sp
            time.sleep(1)
            data.append(sp)#把每一页爬取到的内容写入data列表以便后面存储数据
        save_data(data,key)#把data列表和爬取的某个关键字key，传入存储函数save_data（）

def spider():
    pageSource = driver.page_source#获取源代码
    soup = BeautifulSoup(pageSource,'html.parser')#用bs的方法解析
    list_cont1 = soup.find_all('td',class_='zblist_xm')#可以用这个获取网址href和标题
    list_cont2 = soup.find_all('td',class_='color_9')#可以用来获取日期
    title_list = []#标题列表
    date_list = []#日期列表
    href_list = []#网址列表
    for i in list_cont2:#获取每一个网址和标题
        date = i.text
        date_list.append(date)

    for i in list_cont1:#获取每一个日期
        title = i.find('a').text
        href_ = i.find('a')['href']
        title_list.append(title)
        href_list.append(href_)

    list_all = []#这个是每一页的数据后面要把每一页的数据加到data列表中
    for i in range(len(date_list)):
        list_all.append([date_list[i],title_list[i],href_list[i]])#在当前页面把所有爬取到的数据放到list_all中
    print(len(list_all))#打印数据的长度
    return(list_all)

def save_data(data,key):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'new title'
    sheet['A1'] = 'date'
    sheet['B1'] = 'title'
    sheet['C1'] = 'href'
    for i in data:
        for i in i:
            sheet.append(i)
    wb.save('%s.xlsx'%key)
    
def main():
    get_html()
    end = time.time()
    print('所用的时间为%d'%(end-start))


main()