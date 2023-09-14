import requests
from requests.cookies import RequestsCookieJar


def get_html(url):
    cookies_jar = RequestsCookieJar()
    # cookies_jar.set('BAIDUID_BFESS', '689762E5FF901076535B13B737D78770:FG=1', domain="baike.baidu.com")
    

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0'
    # cookie = 'RT="z=1&dm=baidu.com&si=77600cb6-5d3a-427e-b618-a0bdd2dc2738&ss=ljjocv84&sl=p&tt=ga0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&nu=468vwj63&cl=5byz&ul=5gs7&hd=5h1s"; BAIDUID=689762E5FF901076535B13B737D78770:FG=1; BIDUPSID=689762E5FF901076F1458281944F02E1; PSTM=1688196220; delPer=0; PSINO=5; H_PS_PSSID=36550_38858_38799_38958_38954_38832_38918_38972_38801_38640_26350_38571; BA_HECTOR=208l250lak0galah25ah25261i9vl3v1p; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZFY=p6Qd86lBuox9ovlIvdRuFu4v:BZ5sVAGM7qNn4rmOFN4:C; X_ST_FLOW=0; baikeVisitId=4e243190-e5bc-4a36-a086-56c20f30d99f; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1688196228; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1688196328; ab_sr=1.0.1_YWU0NTQ4ZTEzMWQ3ZTlmYmMzODgyNDBjNjA1NjdkYWRhODE2ZDdlMzk5MDE2NWEyYTNhZjJhMzJjZWQ3MmFjZjRhMmU2YjkwYTI1MDc2YWY5MWUwOTUxZWM0YzQxMWY2MWUyYmI0YzMyNDg4ZTNkNDliNzhjYTg2MjczNjVlZGZmNWU5MTg5YmQ5NDVmMWZjYjI4YzRiY2NmNTdjZDkwZg==; BK_SEARCHLOG=%7B%22key%22%3A%5B%22%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%22%5D%7D'
    cookie1 = RT="z=1&dm=baidu.com&si=77600cb6-5d3a-427e-b618-a0bdd2dc2738&ss=ljjqddtq&sl=g&tt=7r7&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=k5j5&ul=kaoa"
    headers = {'User-Agent': user_agent}

    
    m = requests.get('https://baike.baidu.com', headers={'User-Agent': user_agent, 'Cookie': cookie1})
    print(m.cookies)
    cookies_jar.set('BAIDUID_BFESS', 'E39FA6BFEC4D25077385D96263196C9E:FG=1', domain="baike.baidu.com")
    cookies_jar.set('X_ST_FLOW', '0', domain="baike.baidu.com")
    r = requests.get(url, headers=headers, cookies=cookies_jar, verify=False)
    print(r.text)

get_html('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB')
