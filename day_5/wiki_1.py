''' 《Python网络数据采集》 教程学习 '''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())
def getlinks(url):
    html = urlopen('http://en.wikipedia.org'+url)
    bsobj = BeautifulSoup(html,'lxml')
    return bsobj.find('div',{'id':'bodyContent'}).findAll('a',
                                                          href=re.compile('^(/wiki/)((?!:).)*$'))
links = getlinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newurl = links[random.randint(0,len(links)-1)].attrs['href']
    print(newurl)
    links = getlinks(newurl)