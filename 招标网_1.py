import requests,openpyxl
from bs4 import BeautifulSoup



def createxcel():
    wb = openpyxl.Workbook() 
    sheet = wb.active
    sheet.title = 'new title'
    sheet['A1'] = 'date'
    sheet['B1'] = 'location'
    sheet['C1'] = 'title'
    sheet['D1'] = 'href'




def keywords():
    global kw,page
    kw = []
    x=1
    
    while x:
        word = input('请输入想要查询的内容')
        choose = input('想要继续输入请按回车,否则输入n')
        kw.append(word)
        if choose=='n':
            break
    page = int(input('请输入想要打印的页数'))

def spider():
    # createxcel()
    keywords()
    for i in kw:
        for x in range(page):

            # params={
            # 'kw': '电气',
            # 'page': str(x)
            # }


            url = 'https://www.zbytb.com/zb/search.php?kw='
            res_html = requests.get(url+'%s+&page=%d'%(i,x+1))
            bs_html = BeautifulSoup(res_html.text,'html.parser')
            print(bs_html.text)
            list_cont1 = bs_html.find_all('td',class_='zblist_xm')
            list_cont2 = bs_html.find_all('td',class_='color_9')
            title_list = []
            date_list = []
            href_list = []
            # pattern = r'(\d{4}[\D]\d{1,2}[\D]\d{1,2}[\D]?)'
            #爬取时间
            for i in list_cont2:
                date = i.text
                date_list.append(date)
                # try:
                #     date = re.search(pattern, i.text)  
                #     if date:
                #         date_list.append(date.group(1)) #把用正则表达式清洗过的列表加入时间的列表   
                # except AttributeError():
                #     pass
            #爬取地点和标题
            for i in list_cont1:
                title = i.find('a').text
                href_ = i.find('a')['href']
                title_list.append(title)
                href_list.append(href_)
                # try:
                #     title_list.append(title.text)

                # except AttributeError:
                #     pass
            # for i in title_list:
            #     if len(i)<1:
            #         title_list.remove(i)
            
            # loc_list = title_list[::2]#地点的列表
            # titles_list = title_list[1::2]#标题的列表
            print(len(title_list),len(date_list),len(href_list))
            print(title_list,date_list,href_list)


spider()

# wb.save('zbw.xlsx')