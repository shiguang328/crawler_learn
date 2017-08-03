''' 《Python网络数据采集》 Page27，爬取维基百科某个词条内的其他词条链接。 '''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Eric_Idle')
bsobj = BeautifulSoup(html,'lxml')

# 所有a标签的链接
# for link in bsobj.find_all('a'):
#     if 'href'in link.attrs:
#         print(link.attrs['href'])

# 过滤其他标签，只保留词条链接标签
for link in bsobj.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])