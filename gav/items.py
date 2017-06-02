# -*- coding: utf-8 -*-

import scrapy


class GavItem(scrapy.Item):
    fh = scrapy.Field()
    title = scrapy.Field()
    image_urls = scrapy.Field()

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()