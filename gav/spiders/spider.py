# -*- coding:utf-8 -*-
import sys
import scrapy
from gav.items import GavItem
from gav.items import ImageItem


reload(sys)
sys.setdefaultencoding('utf-8')

class GavSpider(scrapy.Spider):
    name = 'gav'
    allowed_domains = [
        'gavbus1.com',
        'gavbus2.com',
        'gavbus3.com',
        'gavbus4.com',
        'gavbus5.com',
        'gavbus6.com',
        'gavbus7.com',
        'gavbus8.com',
        'gavbus9.com',
        'gavbus88.com',
        'gavbus99.com',
        'gavbus66.com',
        'gavbus.com'
    ]
    start_urls = [
        'https://www.gavbus6.com/page/1',
        'https://www.gavbus3.com/uncensored/page/1',
        'https://www.gavbus9.com/western/page/1',

    ]

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS':{
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'
        },
    }

    def parse(self, response):
        for url in response.xpath('//*[@class="movie-box"]/@href').extract():
            avurl = 'https://www.gavbus6.com' + url
            yield scrapy.Request(avurl, callback=self.parse_item)
        for u in response.xpath('//*[@class="active"]/span/text()').extract():
            if not u:
                continue
        next_page = int(u) + 1
        nexturl = 'https://www.gavbus6.com/page/' + str(next_page)
        yield scrapy.Request(nexturl, callback=self.parse)

    def parse_item(self, response):
        item = GavItem()
        item['fh'] = response.xpath('/html/body/div[6]/div[1]/div[2]/p[1]/span[2]/text()').extract()
        item['title'] = response.xpath('/html/body/div[6]/h3/text()').extract()
        imgurl = response.xpath('/html/body/div[6]/div[1]/div[1]/a/img/@src').extract()
        item['image_urls'] = [imgurl[0] if 'https:' in imgurl[0] else ('https:'+imgurl[0])]
        yield item
