# -*- coding:UTF-8 -*-
# 下载整篇文章
from urllib import request
from bs4 import BeautifulSoup
import html
import re

dr = re.compile(r'<[^>]+>', re.S)  #去除所有html标签的正则表达式

def download_novel(download_url):
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    download_req = request.Request(url = download_url, headers=head)

    download_response = request.urlopen(download_req)
    download_html = download_response.read()
    soup_texts = BeautifulSoup(download_html,"lxml")
    to_str = str(soup_texts.find_all(id='content')).replace('\xa0','')
    to_str = dr.sub('',to_str)
    return to_str

if __name__ == '__main__':
    download_url = 'http://www.xxbiquge.com/6_6873/'  #修真门派掌门路  http://www.xxbiquge.com
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

    download_req = request.Request(url = download_url, headers=head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read()
    soup_texts = BeautifulSoup(download_html,"lxml")
    text_fliter = soup_texts.find_all(id='list')
    soup_list = BeautifulSoup(str(text_fliter), 'lxml')

    f = open('xiuzhenzhangmenlu.txt','w')

    for each in soup_list.find_all('a'):
        print('正在下载: ' + each.get('href'))
        novel = download_novel('http://www.xxbiquge.com'+ each.get('href'))
        f.writelines('\n'+ each.string+ '\n')
        f.write(novel)

    f.close()
    print('下载完成！')

