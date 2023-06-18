import requests
import json
from requests.models import Response
if __name__ == "__main__":
  # 1.指定url
  post_url = 'https://movie.douban.com/j/new_search_subjects'
  paramas = {
    'type': '24',
    'iterval_id':'100:90',
    'actions': '',
    'start': '0',
    'limit': '20'
    # 'sort':'U',
    # 'range':'0,20',
    # 'tags':'',
    # 'start':'0',
    # 'genres':'冒险'
  }
  # 2.进行UA伪装
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
  }
  # 4. 请求发送
  response = requests.get(url=post_url,params=paramas,headers=headers)
  # 5. 获取响应数据: json(方法)
  list_data = response.json()
  # 6. 储存数据
  fp = open('./douban.json','w',encoding='utf-8')
  json.dump(list_data,fp=fp,ensure_ascii=False)

  print("执行完毕!!!")