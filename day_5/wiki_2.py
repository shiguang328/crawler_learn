''' 《Python网络数据采集》 教程学习 '''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
def getlinks(url):
    global pages
    html = urlopen('http://en.wikipedia.org'+url)
    bsobj = BeautifulSoup(html,'lxml')
    try:
        print(bsobj.h1.get_text())
        print(bsobj.find(id='mw-content-text').findAll('p')[0])
        print(bsobj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('The page missing some attribute!')

    for link in bsobj.find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # we got new link
                newpage = link.attrs['href']
                print('-------------------\n'+newpage)
                pages.add(newpage)
                getlinks(newpage)

getlinks('')