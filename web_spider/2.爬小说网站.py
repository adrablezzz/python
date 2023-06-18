import requests
from bs4 import BeautifulSoup
# http请求
def http_request(url):
    target = url
    req = requests.get(url=target)
    return BeautifulSoup(req.text)

# 获取章节内容
def get_book_chapter(url):
    bf = http_request(url)
    title = bf.select('.bookname h1')[0].text
    texts = bf.find_all('div', id='content')
    content = texts[0].text.replace('\xa0'*4, '\n\n')
    return title + '\n\n' + content

# 获取小说章节目录
def get_book_directory(url):
    bf = http_request(url)
    all_directory_list = bf.select('#list dd a, #list center')
    directory_list = handle_directory_list(all_directory_list)
    return directory_list

# 章节目录列表处理函数
def handle_directory_list(list):
    res = []
    index = 0
    for i in range(len(list)):
        item = list[i]
        if(item.get('class') and 'clear' in item.get('class')):
            index = i
        obj = {'title': item.string or '', 'url': item.get('href') or ''}
        res.append(obj)
    # return res[index+1:]
    return res[index+1:15]

# 获取整本小说
def get_book(url):
    directory = get_book_directory(url)
    chapters = ''
    for i in directory:
        chapter_item = get_book_chapter(url + '/' + i['url'])
        chapters += chapter_item + '\n'*4
    writer('./out', '三体', chapters)

def writer(out_path, txt_name, text=''):
    with open('{}/{}.txt'.format(out_path, txt_name), 'w', encoding='utf-8') as f:
        f.writelines(text)
        f.write('\n\n')
BASE_URL = 'https://www.biqudd.com'

# chapter_url = BASE_URL + '/86_86695/25798192.html'
# print(get_book_chapter(chapter_url))

book_url = BASE_URL + '/86_86695'
get_book(book_url)

# writer('./out', '三体', '红岸基地')