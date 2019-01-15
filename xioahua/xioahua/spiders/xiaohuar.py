# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from xioahua.items import XioahuaItem
import time


class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua/']
    url_set = set()

    def parse(self, response):
        a_list = Selector(response).xpath('//div[@class="img"]/a')
        for a in a_list:
            detail_url = a.xpath('.//@href').extract_first()
            title = a.xpath('./img/@alt').extract_first()
            if detail_url in self.url_set:
                pass
            else:
                self.url_set.add(detail_url)
                detail_url = detail_url.replace('/p', '/s')
            yield scrapy.Request(
                url=detail_url, callback=self.second_html,
                meta={
                    'title': title
                }
            )
        for x in range(1, 44):
            next_page = f'http://www.xiaohuar.com/list-1-{x}.html'
            # if x == 43:
            #     print('正在爬取最后一页')
            # else:
            #     print(f'正在爬取第{x}页')
            yield scrapy.Request(
                url=next_page,
                # callback没有指定默认回调parse 函数
            )

    def second_html(self, response):
        title = response.meta.get('title')
        b_list = Selector(response).xpath('//div[@class="pic_img_gallery ad-thumbs"]/ul/li/div/a/@href').extract()
        # b_list = Selector(response).xpath('//ul[@class="photo_ul"]/li/div/a/img/@src').extract()
        for img in b_list:
            # if '/small' in img:
            #     # pattern = re.compile(r'(.*?)small(.*？)15')
            #     # res = re.findall(pattern, img)
            #     # img = ''.join('http://www.xiaohuar.com' + res[0][0] + res[0][1] + '.jpg')
            #     img = img[0:-14].replace('/small', '/') + '.jpg'
            #     img = ''.join('http://www.xiaohuar.com' + img)
            # if '/small' and '.png' in img:
            #     b = img[0:-14].replace('/small', '/') + '.png'
            # if '/small' and '.jpg' in img:
            #     b = img[0:-14].replace('/small', '/') + '.jpg'
            if 'd/file/' in img:
                img = ''.join('http://www.xiaohuar.com' + img)
            item = XioahuaItem()
            item['title'] = title
            item['img_url'] = img
            item['img_name'] = img.split('/')[-1]
            yield item



#         http://www.xiaohuar.com/s-1-2010.html#p2(高清大图)
# /d/file/20181216/smalla1b386aa7989cdd9c8d58ca64fb217671544975719.jpg


