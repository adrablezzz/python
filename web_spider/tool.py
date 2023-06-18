import requests
from bs4 import BeautifulSoup
# http请求
def http_request(url):
    target = url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Cookie': 'Hm_lvt_094775c050f5046091b59ab43cd68c32=1687019133,1687066316; Hm_lvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687019133,1687066316; __gads=ID=bbc4c62b378eb33e-22cc6908a9b4005c:T=1687019134:RT=1687068298:S=ALNI_MYtU7E1FuIXyy8iWT5pFMwXqgQ_SQ; __gpi=UID=00000c50c84c561e:T=1687019134:RT=1687068298:S=ALNI_Ma_OTMWPllgZ9lWfG3_Ew2X97Y6Xg; Hm_lpvt_094775c050f5046091b59ab43cd68c32=1687100879; Hm_lpvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687100879; cf_chl_2=bb7582c19847ce5; cf_clearance=5bUS.nWd7vI8UjpM1q7uZu7ecVp9NfDEL5zJpmorX.I-1687100188-0-160; jieqiVisitTime=jieqiArticlesearchTime%3D1687100879'
    }
    req = requests.get(url=target, headers=headers)
    return BeautifulSoup(req.text, 'html.parser')

# 列表过滤
def my_filter(list, f):
    res = []
    for i in list:
        if(f(i)):
            res.append(i)
    return res

# 列表map
def my_map(list, f):
    res = []
    for i in list:
        res.append(f(i))
    return res

