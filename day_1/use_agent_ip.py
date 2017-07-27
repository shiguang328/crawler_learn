from urllib import request

if __name__ == "__main__":
    url = 'http://www.whatismyip.com.tw/'
    #url = 'http://www.baidu.com'
    # 设置代理IP
    proxy = {'http' : '110.216.67.160:80'}
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_support)

    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                                ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]
    # 安装Opener
    #request.install_opener(opener)

    response = request.urlopen(url)
    html = response.read().decode('utf-8')
    print(html)