from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
    from_data = {}
    from_data['type'] = "AUTO"
    from_data['i'] = "love"
    from_data['doctype'] = "simple"
    #from_data['smartresult'] = "dict"
    from_data['version'] = "2.1"
    from_data['ue'] = "UTF-8"
    from_data['keyfrom'] = "fanyi.web"
    from_data['action'] = "FY_BY_CLICKBUTTON"
    from_data['typoResult'] = "true"

    data = parse.urlencode(from_data).encode('utf-8')
    response = request.urlopen(Request_URL,data)
    html = response.read().decode('utf-8')
    #print(html)
    translate_result = json.loads(html)
    translate_result = translate_result['translateResult']
    print(translate_result)

