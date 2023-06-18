from tool import http_request
from tool import my_filter
from tool import my_map
import time

# 笔趣阁
class Downloader:
    base_url = ''
    book_path = ''
    book_url = ''
    book_name = ''
    out_path = ''
    directorys = []
    rewrite_flag = True
    search_list = []

    def __init__(self, base_url, book_path, book_name='小说', out_path='./out') -> None:
        self.base_url = base_url
        self.book_path = book_path
        self.book_url = '{}/{}'.format(base_url, book_path)
        self.book_name = book_name
        self.out_path = out_path
    
    def start_download(self):
        self.get_book_directory()
        for i in range(len(self.directorys)):
            item = self.directorys[i]
            item_content = self.get_book_chapter(self.book_url + '/' + item['url'])
            self.writer(item_content)
            print('下载中：{:.2%}'.format((i+1)/len(self.directorys)))
            time.sleep(0.5) # 防止服务器反dos机制关闭连接
        print('下载完成')

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
        return res[index+1:]

    def writer(self, text=''):
        if(self.rewrite_flag):
            open('{}/{}.txt'.format(self.out_path, self.book_name), 'w').close()
            self.rewrite_flag = False

        with open('{}/{}.txt'.format(self.out_path, self.book_name), 'a', encoding='utf-8') as f:
            f.writelines(text)
            f.write('\n\n')

    # 搜索小说 需要绕过反爬虫验证
    def search_book(self, book_name):
        search_url = 'https://www.biqudd.com/modules/article/search.php?searchkey=%C8%FD%CC%E5'
        response = http_request(search_url)
        book_list = response.select('.novelslistss a')
        def f(i):
            return book_name in i.string
        filtered_list = my_filter(book_list, f)
        def mf(i):
            return {'title': i.string, 'url': i.get('href')}
        self.search_list = my_map(filtered_list, mf)
        print(self.search_list)
        pass


BASE_URL = 'https://www.biqudd.com'
BOOK_PATH = '/86_86695'
dl = Downloader(base_url=BASE_URL, book_path=BOOK_PATH, book_name='三体')
# dl.start_download()
dl.search_book('三体')