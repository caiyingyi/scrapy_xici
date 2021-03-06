# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



from pymongo import MongoClient
from scrapy.conf import settings

class XiciPipeline(object):

     def __init__(self):
        connection = MongoClient(
            settings[ 'MONGODB_SERVER' ],
            settings[ 'MONGODB_PORT' ]
        )
        db = connection[settings[ 'MONGODB_DB' ]]
        self.collection = db[settings[ 'MONGODB_COLLECTION' ]]

     def process_item(self, item, spider):
        ip = item['ip']
        port=item['port']

        print u"可用的ip："+ ip
        print u"可用的端口："+ port

        self.collection.insert(dict(item))
        return item


