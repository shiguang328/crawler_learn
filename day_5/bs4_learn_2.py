''' 《Python网络数据采集》 Page18，BeautifulSoup学习代码。 '''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html,'lxml')

# 正则表达式和BeautifulSoup的结合使用：匹配制定路径的图片
images = bsObj.find_all('img',{'src':re.compile(r'../img/gifts/img.*.jpg')})
for image in images:
    print(image['src'])