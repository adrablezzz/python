import requests
from bs4 import BeautifulSoup
# http请求
def http_request(url):
    target = url
    req = requests.get(url=target)
    return BeautifulSoup(req.text)