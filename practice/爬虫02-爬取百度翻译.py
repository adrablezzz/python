import requests
import json
from requests.models import Response
if __name__ == "__main__":
  # 1.指定url
  post_url = 'https://fanyi.baidu.com/sug'
  # 2.进行UA伪装
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0'
  }
  # 3. post请求参数处理
  word = input("请输入要翻译的内容:")
  data = {
    'kw': word
  }
  # 4. 请求发送
  response = requests.post(url=post_url,data=data,headers=headers)
  # 5. 获取响应数据: json(方法)
  dic_obj = response.json()
  # 6. 储存数据
  fileName = word + '.json'
  fp = open(fileName,'w',encoding='utf-8')
  json.dump(dic_obj,fp=fp,ensure_ascii=False)

  print("执行完毕!!!")