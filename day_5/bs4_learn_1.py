''' 《Python网络数据采集》 Page18，BeautifulSoup学习代码。 '''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html,'lxml')

# for child in bsObj.find('table',{'id':'giftList'}).children:
#     print(child)

# for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
#     [print(sibling)]

#查找父标签
print(bsObj.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())