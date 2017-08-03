''' 《Python网络数据采集》 Page28，逐个爬取。 '''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())
def getlinks(url):
    html = urlopen('http://wikipedia.org'+url)
    bsobj = BeautifulSoup(html,'lxml')
    return bsobj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))

links = getlinks('/wiki/Kevin_Bacon')
while len(links):
    newUrl = links[random.randint[0,len(links)-1]].attrs['href']
    print(newUrl)
    links = getlinks(newUrl)


# 所有a标签的链接
# for link in bsobj.find_all('a'):
#     if 'href'in link.attrs:
#         print(link.attrs['href'])

# 过滤其他标签，只保留词条链接标签
for link in bsobj.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])