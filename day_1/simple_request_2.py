from urllib import request
import chardet

if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    print('response.geturl() -> %s' % response.geturl())
    print('response.info() -> %s' % response.info())
    print('response.getcode() -> %s' % response.getcode())