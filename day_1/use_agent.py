from urllib import request

# 添加代理，假装浏览器访问
# if __name__ == "__main__":
#     url = 'http://www.csdn.net/'
#     head = {}
#     head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ' \
#                          '(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
#     req = request.Request(url, headers=head)
#     #req = request.Request(url)
#     response = request.urlopen(req)
#     html = response.read().decode('utf-8')
#     print(html)


# 方法二: 后添加header
if __name__ == "__main__":
    url = 'http://www.csdn.net/'
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
                                ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)