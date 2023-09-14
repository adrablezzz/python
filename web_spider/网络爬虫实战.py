from bs4 import BeautifulSoup

# html_str = open('./web_spider/index.html', encoding='utf-8')

# soup = BeautifulSoup(html_str, 'html', from_encoding='utf-8')

# print(soup.prettify())

# Tag:(标签)
# print(soup.title)
# print(soup.a)
# print(soup.p)
# print(soup.name)
# print(soup.title.name)

# soup.title.name = 'myTitle'
# print(soup.title)
# print(soup.myTitle)

# print(soup.p['class'])
# print(soup.p.get('class'))

# print(soup.p.attrs)
# 修改属性...

# NavigableString(标签内部文字)
# print(soup.p.string)

# BeautifulSoup

# Comment(注释)
# print(soup.p.string) #-> None
# print(type(soup.p.string))


# 遍历文档树

# print(soup.head.contents)

# for i in soup.head.children:
#     print(i)

# descendants对子节点后代递归循环
# for i in soup.descendants:
#     print(i)

# strings 对子节点后代文字内容递归循环
# for i in soup.strings:
#     print(repr(i))

# stripped_strings 去除空格换行
# for i in soup.stripped_strings:
#     print(repr(i))

# 父级 .parent .parents
# 兄弟 .next_sibling .prev_sibling  .next_siblings .prev_siblings
# 前后节点 .next_element .previous_element  .next_elements .previous_elements

# 搜索文档树
# print(soup.find_all('a')) #还可以传入正则，包括以下
# print(soup.find_all(['a', 'p']))
# print(soup.find_all(id='main'))
# print(soup.find_all(class_='p'))
# print(soup.find_all(attrs={'info':'a'}))
# print(soup.find_all(text='百度'))

# print(soup.find_all(class_='p', limit=1))  #限制数量
# print(soup.find_all(class_='p', recursive=False)) #只搜索直接子节点
# 其它...


# css选择器
# print(soup.select('#main'))
# print(soup.select('a[href]')) #查找存在某个属性
# print(soup.select('a[href="www.baidu.com"]')) #查找存在某个属性


# json存储 python对象 =》 json对象
# import json
# jsonData = [{"name":"zs","age":22}]
# jsonStr = json.dumps(jsonData, ensure_ascii=False)
# print(jsonStr)
# with open('out.txt', 'w') as fp:
#     json.dump(jsonStr, fp=fp, ensure_ascii=False)

# json解码 json对象 =》 python对象；
# print(json.loads(jsonStr))
# with open('out.txt', 'r') as fp:
#     print(json.load(fp))


# csv存储
# import csv
# headers = ['id', 'name', 'age', 'country']
# rows = [
#     (1001, '张三', 18, '中国'),
#     (1002, 'lisi', 20, 'UK'),
# ]
# with open('out.csv', 'w', encoding='utf-8-sig', newline='') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)

# from collections import namedtuple
# with open('out.csv', 'r', encoding='utf-8-sig') as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     Row = namedtuple('Row', headers)
#     print(headers)
#     for r in f_csv:
#         row = Row(*r)
#         print(row.name)
#         print(row)


# 多媒体文件抽取
# import requests
# def spiderImages():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
#         'Cookie': 't=eb8ecd4b8b6bc86bf9ecfa04311725c4; r=9858; Hm_lpvt_c13cf8e9faf62071ac13fd4eafaf1acf=1687962315; Hm_lvt_a0c29956538209f8d51a5eede55c74f9=1687961861; Hm_lpvt_a0c29956538209f8d51a5eede55c74f9=1687962315; statistics_clientid=me'
#     }
#     response = requests.get('https://img.ivsky.com/', headers=headers)
#     soup = BeautifulSoup(response.text, 'html', from_encoding='utf-8')
#     imgs = soup.find_all('img')
#     imgList = []
#     for i in imgs:
#         imgList.append(i['src'])
#     return imgList

# list = spiderImages()
# print(list)


# 邮件发送
def sendEmail(to, title, content):
    import smtplib
    from email.header import Header
    from email.mime.text import MIMEText

    from_addr = 'adrablezzz@163.com'
    password = 'YZFBGBOPVCYXVTVU'
    # YZFBGBOPVCYXVTVU
    smtp_server = 'smtp.163.com'

    to_addrs = to

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = Header('Rabot001 <{}>'.format(from_addr))
    msg['To'] = Header(','.join(to_addrs))

    subject = title
    msg['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(smtp_server, 25)
        # smtpObj.set_debuglevel(1)
        smtpObj.login(from_addr, password)
        smtpObj.sendmail(from_addr, to_addrs, msg.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('Error: 发送失败')

# to = ['1942775049@qq.com']
# title = 'python邮件'
# content = '邮件测试信息03...'
# sendEmail(to, title, content)


# 基础爬虫
# 爬虫框架分为5大模块：
'''
爬虫调度器: 协调其它4个模块
URL管理器: 管理URL链接, 维护已爬取和未爬取的URL集合, 提供获取新URL链接的接口
HTML下载器: 从URL管理器获取未爬取的URL链接并下载网页
HTMl解析器: 从HTML下载器中获取已下载的网页, 从中解析出新的URL交给URL管理器,解析出有效数据交给数据存储器
数据存储器: 数据存储器用于将HTML解析器解析出来的数据通过文件或数据库的形式存储起来
'''

# 2.URL管理器
'''
变量: 爬取的url集合, 未爬取的url集合
接口: 
    has_new_url() 判断是否有待取的url
    add_new_urls(urls) 添加新的url到未爬取集合中
    get_new_url() 获取未爬取的url
    new_url_size() 获取未爬取的url集合大小
    old_url_size() 获取已爬取的url集合大小
'''

# 3.HTML下载器
# 注意网页编码
'''
接口: download(url) 下载网页
'''

# 4.HTML解析器
'''
接口: 
    parser 解析网页, 返回url和数据
'''

# 5.数据存储器
'''
方法：
    store_data(data) 将解析出来的数据存储到内存中
    output_html() 将存储的数据输出为指定的文件格式
'''

# 1.爬虫调度器
'''
1. 初始化各个模块
2. 通过crawl(root_url)方法传入入口URL
3. 按照流程控制各个模块
'''

# 简单分布式爬虫
# 1.url管理器
'''
对url进行md5处理,缩减内存 save_progress load_progress
'''
# 2.数据存储器

# 3.控制调度器

# 爬虫节点
'''
HTML下载器
HTML解析器
爬虫调度器
'''


# 数据库 MySQL 
'''
安装MySQL-python: pip install MySQL-python

import MySQLdb
# 连接数据库
con = MySQLdb.connect(host='localhost', user='root', password='',db='test', port='3306', charset='utf-8')
# 建立游标
cur = con.cursor() 
# 建表
cur.execute('CREATE TABLE person (id int not null auto_increment primary key, name varchar(20), age int') 
# 插入数据
cur.execute('INSERT INTO person (name, age) VALUES (%s, %s)', ('zs', 20))
# 插入多条
cur.execuetemany('INSERT INTO person (name, age) VALUES (%s, %s)', [('lisi', 21), ('wangwu',22)])
# 提交 (提交了操作才会生效)
con.commit()
# 如果出现错误回滚
con.rollback()

# 查询
cur.execute('SELECT * FROM person')
# 获取所有数据 -> 返回二维数组
res = cur.fetchall()
# 获取其中一条 -> 返回元组
res = cur.fetchone()

# 修改和删除
cur.execute('UPDATE person SET name=%s WHERE id=%s, ('zhaoliu', 1))
cur.execute('DELETE FROM person WHERE id=%s', (0,))
con.commit()
con.close()
'''


# mongoDB
'''
# 安装 pip install pymongo

import pymongo
# 连接数据库
client = pymongo.MongoClient()
client = pymongo.MongoClient('localhost', 27017)
client = pymongo.MongoClient('mongodb://localhost:27017/')

# 获取数据库
db = client.papers
db = client['pa-pers]

# 获取集合
collection = db.books

# 插入文档
book = {"author": "Mike","text": "My first book!", "tags": ["爬虫", "python", "网络"], "date": datetime.datetime.utcnow()}
book_id = collection.insert(book)
# 批量插入
books = [
    {"author": "Mike","text": "My first book!", "tags": ["爬虫", "python", "网络"], "date": datetime.datetime.utcnow()},
    {"author": "Mike2","text": "My first book2!", "tags": ["爬虫", "python", "网络"], "date": datetime.datetime.utcnow()}
]
book_id = collection.insert(books)

# 查询文档
collection.find_one({"author":"Mike"})
collection.find({"author":"Mike"}).count()

# 修改文档
collection.update({"author":"Mike"},{"$set":{"text":"python book"}})

# 删除文档
collection.remove({"author":"Mike"})
'''


'''
# 动态爬取网站
PhantomJS http://phantomjs.org/
Selenium 
'''


'''
# Scrapy 爬虫架构
Scrapy引擎(Engine)
调度器(Scheduler)
下载器(Downloader)
Spider 分析response返回Item
Item Pipeline 处理Item
下载器中间件
Spider中间件
'''