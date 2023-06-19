import requests
from bs4 import BeautifulSoup
# http get请求

def http_request(url):
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        # 'Cookie': 'Hm_lvt_094775c050f5046091b59ab43cd68c32=1687019133,1687066316; Hm_lvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687019133,1687066316; __gads=ID=bbc4c62b378eb33e-22cc6908a9b4005c:T=1687019134:RT=1687068298:S=ALNI_MYtU7E1FuIXyy8iWT5pFMwXqgQ_SQ; __gpi=UID=00000c50c84c561e:T=1687019134:RT=1687068298:S=ALNI_Ma_OTMWPllgZ9lWfG3_Ew2X97Y6Xg; Hm_lpvt_094775c050f5046091b59ab43cd68c32=1687100879; Hm_lpvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687100879; cf_chl_2=bb7582c19847ce5; cf_clearance=5bUS.nWd7vI8UjpM1q7uZu7ecVp9NfDEL5zJpmorX.I-1687100188-0-160; jieqiVisitTime=jieqiArticlesearchTime%3D1687100879'

        # 2023年6月19日22:22:33 chorme
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        # 'Cookie': 'Hm_lvt_094775c050f5046091b59ab43cd68c32=1687068391,1687182983; Hm_lvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687068391,1687182983; cf_chl_2=92e173fa3dec8f0; cf_clearance=z_mNQKN06uZJHge9T7QyOIzC8.A9PlgR4STdbu8MxMo-1687183004-0-160; jieqiVisitId=article_articleviews%3D86693; __gads=ID=a485432064a7ee99-22a8a73bafe10077:T=1687068392:RT=1687183268:S=ALNI_MYSyj0mPUg7qdi_MyfckVec3BkmTQ; __gpi=UID=00000c5107fd5f03:T=1687068392:RT=1687183268:S=ALNI_MZ6HGkmFxDyIXOJQIQjOWI3eu3gdw; jieqiVisitTime=jieqiArticlesearchTime%3D1687184037; Hm_lpvt_094775c050f5046091b59ab43cd68c32=1687184038; Hm_lpvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687184038',

        # 2023年6月19日22:43:23
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        # 'Cookie': 'Hm_lvt_094775c050f5046091b59ab43cd68c32=1687068391,1687182983; Hm_lvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687068391,1687182983; jieqiVisitId=article_articleviews%3D86693; __gads=ID=a485432064a7ee99-22a8a73bafe10077:T=1687068392:RT=1687183268:S=ALNI_MYSyj0mPUg7qdi_MyfckVec3BkmTQ; __gpi=UID=00000c5107fd5f03:T=1687068392:RT=1687183268:S=ALNI_MZ6HGkmFxDyIXOJQIQjOWI3eu3gdw; cf_chl_2=5489765364bb22c; cf_clearance=MRa_W5UVSTARGuwFnJiQiAAza1A8XHTcU_xcjz5ef4Y-1687185594-0-160; jieqiVisitTime=jieqiArticlesearchTime%3D1687185623; Hm_lpvt_094775c050f5046091b59ab43cd68c32=1687185625; Hm_lpvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687185625'

        # 2023年6月19日23:55:33
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Cookie': 'Hm_lvt_094775c050f5046091b59ab43cd68c32=1687068391,1687182983; Hm_lvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687068391,1687182983; __gads=ID=a485432064a7ee99-22a8a73bafe10077:T=1687068392:RT=1687183268:S=ALNI_MYSyj0mPUg7qdi_MyfckVec3BkmTQ; __gpi=UID=00000c5107fd5f03:T=1687068392:RT=1687183268:S=ALNI_MZ6HGkmFxDyIXOJQIQjOWI3eu3gdw; cf_clearance=LhLt9juUAWpwP6yGygMBwFsI0olrUhoeWHZHKUqDy38-1687190062-0-160; jieqiVisitTime=jieqiArticlesearchTime%3D1687191280; Hm_lpvt_094775c050f5046091b59ab43cd68c32=1687191952; Hm_lpvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687191952; cf_chl_2=6e792d39cf13f69'
    }
    req = requests.get(url, headers=headers)
    return BeautifulSoup(req.text, 'html.parser')

def http_request_post(url, data = {}):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Cookie': 'Hm_lvt_094775c050f5046091b59ab43cd68c32=1687068391,1687182983; Hm_lvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687068391,1687182983; __gads=ID=a485432064a7ee99-22a8a73bafe10077:T=1687068392:RT=1687183268:S=ALNI_MYSyj0mPUg7qdi_MyfckVec3BkmTQ; __gpi=UID=00000c5107fd5f03:T=1687068392:RT=1687183268:S=ALNI_MZ6HGkmFxDyIXOJQIQjOWI3eu3gdw; cf_chl_2=6e792d39cf13f69; cf_clearance=8hdFqlHJ4lSWmMWKw89jg25t6AJFoWblWb0ZalX28.c-1687192133-0-160; jieqiVisitTime=jieqiArticlesearchTime%3D1687192151; Hm_lpvt_094775c050f5046091b59ab43cd68c32=1687192152; Hm_lpvt_a71b1bc761fe3f26085e79b5fd6a7f71=1687192152'
    }
    req = requests.post(url, data, headers=headers)
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

