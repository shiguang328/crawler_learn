from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlretrieve
import time
import os

if __name__ == '__main__':

    target_url = 'http://www.shuaia.net/rihanshuaige/2017-05-18/1294.html'
    filename = '张根硕拍摄机车型男写真帅气十足' + '.jpg'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ' \
                                  '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    req = request.Request(target_url, headers=headers)
    response = request.urlopen(req)
    hmtl = response.read()
    soup = BeautifulSoup(hmtl, 'lxml')
    img_url = soup.find_all('div', class_='wr-single-content-list')
    soup_2 = BeautifulSoup(str(img_url),'lxml')
    img_url = 'http://www.shuaia.net'+ soup_2.div.img.get('src')
    if 'images' not in os.listdir():
        os.makedirs('images')
    urlretrieve(url=img_url,filename='images/'+filename)
    print('下载完成！')