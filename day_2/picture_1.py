from bs4 import BeautifulSoup
from urllib import request
import time

if __name__ == '__main__':
    list_url = []
    for num in range(1,20):
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
print(list_url)