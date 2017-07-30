# -*- coding:UTF-8 -*-
#下载单篇文章
from urllib import request
from bs4 import BeautifulSoup
import html
import re

dr = re.compile(r'<[^>]+>', re.S)  #去除所有html标签的正则表达式

if __name__ == '__main__':
    download_url = 'http://www.xxbiquge.com/6_6873/6165165.html'  #修真门派掌门路  http://www.xxbiquge.com
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
    download_html = download_response.read()
    #print(download_html)
    soup_texts = BeautifulSoup(download_html,"lxml")
    to_str = str(soup_texts.find_all(id='content')).replace('\xa0','')
    #to_str = to_str.replace('<br/>','')
    to_str = dr.sub('',to_str)
    print(to_str)
    with open('chaper.txt','w') as f:
        f.write(to_str)

    # text_format = soup_texts.prettify()
    # print(text_format)
    # with open('novel_web.html','w') as f:
    #     f.write(text_format)
    #text_fliter = soup_texts.find_all(id='list')
    #print(text_fliter)
    #soup_list = BeautifulSoup(str(text_fliter), 'lxml')
    #print('soup_list.div.dl.dd: ',soup_list.div.dl.dd.a)
    #print(soup_list.find_all('a'))
    #     for each in soup_list.find_all('a'):
    #     print(each.get('href'))
    # print('链接采集成功！')

    # temp = soup_list.a
    # print('soup_list.a -> ', temp)
    # print('soup_list.a.next_subling -> ',temp.next_sibling)

    #texts = soup_texts.find_all(id='content', class_='showtxt')
    #print(texts)
    #soup_text = BeautifulSoup(str(texts), 'lxml')
    # 将\xa0无法解码的字符删除
    #print(soup_text.div.text.replace('\xa0',''))
    #print(soup_text.text.replace('\xa0',''))
    #print(soup_text)

