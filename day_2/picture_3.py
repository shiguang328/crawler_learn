from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlretrieve
import time
import os

if __name__ == '__main__':
    list_url = []
    for num in range(1,5):
        if num == 1:
            url = 'http://www.shuaia.net/index.html'
        else:
            url = 'http://www.shuaia.net/index_%d.html' % num
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ' \
                              '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
        req = request.Request(url,headers=headers)
        response = request.urlopen(req)
        hmtl = response.read().decode('utf-8')
        soup = BeautifulSoup(hmtl,'lxml')
        targets_url = soup.find_all(class_='item-img')
        for each in targets_url:
            list_url.append(each.img.get('alt') + '=' + each.get('href'))
        time.sleep(0.5)

    print('连接采集完成。')

    for each_img in list_url:
        img_info = each_img.split('=')
        target_url = img_info[1]
        filename = img_info[0] + '.jpg'
        print('下载：'+filename)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ' \
                                      '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
        req = request.Request(target_url, headers=headers)
        response = request.urlopen(req)
        hmtl = response.read()
        soup = BeautifulSoup(hmtl, 'lxml')
        img_url = soup.find_all('div', class_='wr-single-content-list')
        soup_2 = BeautifulSoup(str(img_url), 'lxml')
        img_url = 'http://www.shuaia.net' + soup_2.div.img.get('src')
        if 'images' not in os.listdir():
            os.makedirs('images')
        urlretrieve(url=img_url, filename='images/' + filename)
        time.sleep(2)
    print('下载完成！')