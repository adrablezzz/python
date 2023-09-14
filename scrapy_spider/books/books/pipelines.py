# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BooksPipeline:
    def __init__(self) -> None:
        self.f = open('三体全.txt', 'wb')

    def process_item(self, item, spider):
        text = item['title'] + '\n' + item['content'] + '\n\n\n\n'

        self.f.write(text.encode('utf-8'))
        return item

    def close_spider(self):
        self.f.close()
