# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Mk11FnacItem(scrapy.Item):
    product_name = scrapy.Field()
    product_platform = scrapy.Field()
    product_sale_price = scrapy.Field()
