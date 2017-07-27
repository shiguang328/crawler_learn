# 保存cookie
# 关于如何使用保存的cookie，请参考cookie_3.py

from urllib import request
from http import cookiejar

if __name__ == '__main__':
    filename = 'cookie_2.txt'
    # 声明一个MozillaCookieJar对象来保存cookie，之后写入文件
    cookie = cookiejar.MozillaCookieJar(filename)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    #ignore_discard的意思是即使cookies将被丢弃也将它保存下来
    #ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入
    cookie.save(ignore_discard=True, ignore_expires=True)
