import hashlib

class UrlManager:
    def __init__(self) -> None:
        self.new_urls = self.load_progress('new_urls.txt') # 未爬取的url集合
        self.old_urls = self.load_progress('old_urls.txt') # 已爬取的url集合
    
    # 是否有未爬取的url
    def has_new_url(self):
        return self.new_url_size() != 0
    
    # 获取一个未爬取的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url)
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url
    
    # 添加一个新的url到未爬取的url集合
    def add_new_url(self, url):
        if url is None:
            return
        m = hashlib.md5()
        m.update(url)
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    # 添加新的urls到未爬取的url集合
    def add_new_urls(self, urls):
        # urls 集合
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 获取未爬取的url集合大小
    def new_url_size(self):
        return len(self.new_urls)
    
    # 获取已爬取的url集合大小
    def old_url_size(self):
        return len(self.old_urls)
    
    # 保存进度 path文件路径 data数据
    def save_progress(self, path, data):
        with open(path, 'wb') as f:
            pass