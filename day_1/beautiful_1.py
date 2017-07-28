# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import html

if __name__ == '__main__':
    download_url = 'http://www.siluke.org/book/81788/26892699.html'  #这个网站可以爬
    #download_url = 'http://www.biqukan.com/1_1094/5403177.html'
    head = {}

    # 设置代理IP
    proxy = {'http': '180.168.179.193:8080'}
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_support)

    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                                        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]
    download_req = request.Request(url = download_url, headers=head)

    #request.install_opener(opener)
    download_response = request.urlopen(download_req)
    #download_response = opener.open(download_url)
    download_html = download_response.read().decode('gbk','ignore')
    #print(download_html)
    soup_texts = BeautifulSoup(download_html,"lxml")
    texts = soup_texts.find_all(id='content', class_='showtxt')
    #print(texts)
    soup_text = BeautifulSoup(str(texts), 'lxml')
    # 将\xa0无法解码的字符删除
    #print(soup_text.div.text.replace('\xa0',''))
    print(soup_text.text.replace('\xa0',''))
    #print(soup_text)

