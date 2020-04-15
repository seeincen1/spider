# -*- coding: utf-8 -*-
import scrapy
from ZhipinSpider.items import ZhipinspiderItem

class JobPositionSpider(scrapy.Spider):
    #定义该sprider的名字
    name = 'job_position'
    #定义该sprider允许爬取的域名
    allowed_domains = ['zhipin.com']
    #定义该sprider允许爬取的首页列表
    start_urls = ['https://www.zhipin.com/c101270100/d_203/?query=python&page=1']

    #提取response所包含的信息
    def parse(self, response):
        for job_primary in response.xpath('//div[@class="job_primary"]'):
            item = ZhipinspiderItem()
            info_primary = job_primary.xpath('./div[@class="info_primary"]')
            item['title'] = info_primary.xpath('./h3/a/div[@class="job_title"]/text()').extract_first()
            item['salary'] = info_primary.xpath('./h3/a/span[@class="red"]/text()').exract_first()
            item['work_addr'] = info_primary.xpath('./p/text()').exract_first()
            item['url'] = info_primary.xpath('./h3/a/@herf').exract_first()
            yield item


