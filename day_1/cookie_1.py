from urllib import request
from http import cookiejar

if __name__ == '__main__':
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcesor对象来创建cookie处理器，也就是CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)

    response = opener.open('http://www.baidu.com')
    # 打印cookie信息
    for item in cookie:
        print('Name = %s' % item.name)
        print('Value = %s' % item.value)

