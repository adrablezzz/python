# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class DemospiderPipeline:
    def __init__(self) -> None:
        self.f = open('out_data.json', 'wb')

    def process_item(self, item, spider):
        content = json.dumps(item, ensure_ascii=False) + ',\n'
        self.f.write(content.encode('utf-8'))
        return item
    
    def close_spider(self):
        self.f.close()
