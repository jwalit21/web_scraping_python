# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3                                                          #code for sqlite3
import mysql.connector

class QuoteTutorialPipeline:
    
    def __init__(self):
            self.create_connection()
            self.create_table()
    
    def create_connection(self):
        
        #self.conn = sqlite3.connect('myquotes.db')                      #code for sqlite3
        
        self.conn = mysql.connector.connect(                             #code for mysql
            host = 'localhost',
            user = 'root',
            passwd = '',
            database = 'web_scraping'
        )
        
        #read sqlite.db file on sqliteonline.com
        
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute(""" drop table if exists quotes_db """)
        self.curr.execute(""" create table quotes_db(
                    quote_title text,
                    author text,
                    tag text
        ) """)

    
    def store_db(self,item):
        
        #code for sqlite3
        #self.curr.execute(""" insert into quotes_db values(?,?,?) """,(
        #    item['quote_title'][0],
        #    item['author'][0],
        #    item['tag'][0],
        #))
        
        self.curr.execute(""" insert into quotes_db values(%s,%s,%s) """,(
            item['quote_title'][0],
            item['author'][0],
            item['tag'][0],
        ))
        
        self.conn.commit()
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
