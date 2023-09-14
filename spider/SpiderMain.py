from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager

class SpiderMain:
    
    def __init__(self) -> None:
        self.manager = UrlManager()
        self.dowloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        # 判断是否有新的url and 抓取的url要限制100
        while(self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                # 从url管理器获取新的url
                new_url = self.manager.get_new_url()
                # html下载器下载网页
                html = self.dowloader.downlaod(new_url)
                # 解析器解析网页
                new_urls,data = self.parser.parser(new_url, html)
                # 将解析的url添加到url管理器
                self.manager.add_new_urls(new_urls)
                # 存储器存储文件
                self.output.store_data(data)
                print('已抓取{}个链接'.format(self.manager.old_url_size()))
            except Exception:
                print('爬取失败')
        self.output.output_html()

if __name__ == '__main__':
    spider_main = SpiderMain()
    spider_main.crawl('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB')
