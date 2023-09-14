class UrlManager:
    def __init__(self) -> None:
        self.new_urls = set() # 未爬取的
        self.old_urls = set() # 已爬取的
    
    def has_new_url(self) -> bool:
        return self.new_url_size() != 0

    def add_new_url(self, url:str) -> None:
        # @params: url 
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls:set) -> None:
        # @params: urls requireType set
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_new_url(self) -> str:
        # 获取一个未爬取的url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def new_url_size(self) -> int:
        return len(self.new_urls)

    def old_url_size(self) -> int:
        return len(self.old_urls)