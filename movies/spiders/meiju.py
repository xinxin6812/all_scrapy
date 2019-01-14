# -*- coding: utf-8 -*-
import scrapy


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
        # //ul[@class="top-list  fn-clear"]/li/h5/text()
        pass
