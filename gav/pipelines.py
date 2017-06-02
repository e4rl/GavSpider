# -*- coding: utf-8 -*-

import json
import codecs
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class GavPipeline(object):
    def __init__(self):
        self.file = codecs.open('gav.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        return item

class GavImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return 'images/%s' % (image_guid)

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item