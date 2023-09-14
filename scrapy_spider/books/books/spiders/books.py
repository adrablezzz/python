import scrapy


class Books(scrapy.Spider):
    name = 'books'
    start_urls = [
        'http://www.ujxsw.net/read/7554/6576638.html'
    ]

    def parse(self, response):
        title = response.xpath("//h3[@class='zhangj']/text()").extract()[0]
        content_arr = response.xpath("//div[@class='read-content']/p/text()").extract()
        content = ''.join(content_arr).replace('\xa0', '')
        yield {
            'title': title,
            'content': content
        }
        if title == '第1章 科学边界(1)':
            next_page = response.xpath("//p[@class='mlfy_page']/a[3]/@href").extract()[0]
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
