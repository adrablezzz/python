import requests, json, re
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib import request

class PictureSpider:
    base_url = ''
    pictures = []

    def __init__(self, base_url) -> None:
        self.base_url = base_url
    
    def get_pictures(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        req = requests.get(url=self.base_url, verify=False, headers=headers)
        json_data = json.loads(req.text)
        with open('htto_data.txt', 'w', encoding='utf-8') as f:
            f.write(str(json_data))
        data_list = json_data['data']
        for item in data_list:
            if(item):
                name = re.sub('<[^>]*>', '', item['fromPageTitle'])
                pic = {'name': name, 'url': item['thumbURL']}
                self.pictures.append(pic)
        print('获取图片成功')
        print('共有{}条数据'.format(len(self.pictures)))

    def download(self):
        print('开始下载...')
        for i in self.pictures:
            request.urlretrieve(i['url'], i['name'] + '.jpg')
        print('下载完成')

if __name__ == '__main__':
    search_key = input('请输入要搜索的图片描述：')
    page = 1
    page_size = 10
    pn = (page-1) * page_size
    rn = page_size
    target = '''
        https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9628828529995670699&ipn=rj&ct=201326592&is=&fp=result&fr=
        &word={w}&queryWord={w}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=
        &height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={pn}&rn={rn}&gsm=5a&1687274626585=
        '''.format(w=quote(search_key), pn=pn, rn=rn)
    ps = PictureSpider(base_url=target)
    ps.get_pictures()
    ps.download()