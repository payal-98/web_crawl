# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class CrawlingPipeline(object):
    
    def __init__(self):
        self.create_connection()
        self.create_table()
        
    def create_connection(self):
        self.conn =sqlite3.connect("mymovie.db")
        self.curr=self.conn.cursor()
        
    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS movie_tb""")
        self.curr.execute(""" create table movie_tb(title text,img text)""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
        
    def store_db(self,item):
        self.curr.execute("""insert into movie_tb values (?,?)""",(
            item['name'][0],
            item['img'][0]
        ))
        self.conn.commit()