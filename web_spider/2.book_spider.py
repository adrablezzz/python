from tool import http_request
from tool import http_request_post
from tool import my_filter
from tool import my_map
import time, sys
from bs4 import BeautifulSoup

# 笔趣阁
class Downloader:
    book_url = ''
    book_name = ''
    directorys = []
    rewrite_flag = True
    search_list = []

    def __init__(self) -> None:
        pass
    
    def start_download(self):
        print('《{}》请求中...'.format(self.book_name))
        self.get_book_directory()
        print('《{}》开始下载'.format(self.book_name))
        length = len(self.directorys)
        for i in range(length):
            sys.stdout.write('  下载中：{:.2%}\r'.format(i/length))
            sys.stdout.flush()
            time.sleep(0.5) # 防止服务器反dos机制关闭连接

            item = self.directorys[i]
            item_content = self.get_book_chapter(self.book_url + '/' + item['url'])
            self.writer(item_content)
        print('《{}》下载完成：100%'.format(self.book_name))

    # 获取章节内容
    def get_book_chapter(self, url):
        bf = http_request(url)
        title = bf.select('.bookname h1')[0].text
        texts = bf.find_all('div', id='content')
        content = texts[0].text.replace('\xa0'*4, '\n\n')
        return title + '\n\n' + content + '\n'*4

    # 获取小说章节目录
    def get_book_directory(self):
        bf = http_request(self.book_url)
        all_directory_list = bf.select('#list dd a, #list center')
        self.directorys = self.handle_directory_list(all_directory_list)

    # 章节目录列表处理函数
    def handle_directory_list(self, list):
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

    def writer(self, text=''):
        if(self.rewrite_flag):
            open('{}.txt'.format(self.book_name), 'w').close()
            self.rewrite_flag = False

        with open('{}.txt'.format(self.book_name), 'a', encoding='utf-8') as f:
            f.writelines(text)
            f.write('\n\n')

    # 搜索小说 需要绕过反爬虫验证
    def search_book(self, search_key=''):
        search_url = 'https://www.biqudd.com/modules/article/search.php?searchkey=' + search_key
        response = http_request(search_url)
        with open('error_page.txt', 'w', encoding='utf-8') as f:
            f.writelines(str(response))
        book_list = response.select('.novelslistss a')
        def f(i):
            return search_key in i.string
        filtered_list = my_filter(book_list, f)
        def mf(i):
            return {'title': i.string, 'url': i.get('href')}
        self.search_list = my_map(filtered_list, mf)
    
    def search_book_post(self, search_key=''):
        search_url = 'https://www.biqudd.com/modules/article/search.php'
        response = http_request_post(search_url, data={'searchtype': 'articlename', 'searchkey': search_key.encode('gbk')})
        with open('error_page.txt', 'w', encoding='utf-8') as f:
            f.writelines(str(response))
        book_list = response.select('.novelslistss li')
        def mf(item):
            i = BeautifulSoup(str(item), 'html.parser')
            book_link = i.select('.s2 a')[0]
            author_name = i.select('.s4')[0].string
            return {'title': book_link.string, 'url': book_link.get('href'), 'author': author_name}
        self.search_list = my_map(book_list, mf)
        print(self.search_list)


    def set_downloader(self, book_name, book_url):
        self.book_name = book_name
        self.book_url = book_url


if __name__ == '__main__':
    BASE_URL = 'https://www.biqudd.com'
    print('欢迎使用小说下载器！(书籍来源：{})'.format(BASE_URL))
    search_key = input('请输入书名(宁缺勿多)：')
    dl = Downloader()
    dl.search_book_post(search_key)
    if(len(dl.search_list) > 0):
        list_str = ''
        for i in range(len(dl.search_list)):
            list_str += '{} - {} - {}\n'.format(i, dl.search_list[i]['title'], dl.search_list[i]['author'])
        index = eval(input('搜索到以下书籍，请输入数字进行选择：\n' + list_str))
        choice = dl.search_list[index*1]
        dl.set_downloader(choice['title'], choice['url'])
        dl.start_download()
    else:
        print('未搜索到相关书籍！')