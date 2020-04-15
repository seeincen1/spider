# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class ZhipinspiderPipeline(object):

        #创建mogo数据库链接
    dbclient = pymongo.MongoClient('localhost',27017)
    zhipin = dbclient['zhipin']

    def process_item(self, item, spider):

        item = ZhipinspiderPipeline.zhipin.insert_one(item)


        return item
