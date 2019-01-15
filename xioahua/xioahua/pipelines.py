# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import os
from urllib import request


class XioahuaPipeline(object):
    def process_item(self, item, spider):
        if not os.path.exists(item['title']):
            os.mkdir(item['title'])
        path = item['title'] + '/' + item['img_name']
        if not os.path.exists(path):
            print(f"\r 正在保存{item['title']}， {item['img_url']}")
            request.urlretrieve(item['img_url'], path)
        else:
            print(f"\r {item['title']}该图片已存在")
        return item

