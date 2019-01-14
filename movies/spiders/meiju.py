# -*- coding: utf-8 -*-
import scrapy
from movies.items import MoviesItem

import time
class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        """
        解析页面
        :param response:
        :return:
        """
        # 获取剧集名
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movies:
            name = movie.xpath('./h5/a/text()').extract_first()
            # state = movie.xpath('//span/font/text()').extract()
            # print(name)
            item = MoviesItem()
            item['name'] = name
            yield item

