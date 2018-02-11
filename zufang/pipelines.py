# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ZufangPipeline(object):
    def open_spider(self,spider):
        self.con = sqlite3.connect("zufang.sqlite")
        self.cu = self.con.cursor()
    def process_item(self, item, spider):
        print(spider.name)
        inser_sqlite = "insert into zufang (title,money) values('{}','{}')".format(item['title'],item['money'])
        print(inser_sqlite)
        self.cu.execute(inser_sqlite)
        self.con.commit()
        return item
    def close_spider(self,spider):
        self.con.close()