# 从文件中获取cookie，并访问
#关于如何保存cookie请参考cookie_2.py

from urllib import request
from http import cookiejar

if __name__ == '__main__':
    filename = 'cookie_2.txt'  # 相对路径
    cookie = cookiejar.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))