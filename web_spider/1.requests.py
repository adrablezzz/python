import requests
def http_request():
    target = 'http://gitbook.cn/'
    req = requests.get(url=target)
    print(req.text)
http_request()