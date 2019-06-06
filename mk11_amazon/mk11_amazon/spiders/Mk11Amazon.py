# -*- coding: utf-8 -*-
import scrapy
from mk11_amazon.items import Mk11AmazonItem


class Mk11amazonSpider(scrapy.Spider):
    name = "Mk11Amazon"
    allowed_domains = ["amazon.fr"]
    start_urls = [
        "https://www.amazon.fr//dp/B07KZ4H8B6", # xone standard
        "https://www.amazon.fr/dp/B07KZHVJT8", # xone premium
        "https://www.amazon.fr/dp/B07MWZ5NZL", # xone kollector
        "https://www.amazon.fr/dp/B07KZHVJT7", # ps4 standard
        "https://www.amazon.fr/dp/B07KZY8QN9", # ps4 premium
        "https://www.amazon.fr/dp/B07MWXTN89", # ps4 kollector
        "https://www.amazon.fr/dp/B07L9FVQFW", # switch standard
        "https://www.amazon.fr/dp/B07N246D7G", # pc kollector
        ]

    def parse(self, response):
        items = Mk11AmazonItem()
        title = response.xpath('//h1[@id="title"]/span/text()').extract()
        platform = response.xpath(
            '//div[@id="platformInformation_feature_div"]/text()'
        ).extract()
        sale_price = response.xpath(
            '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
        ).extract()
        availability = response.xpath('//div[@id="availability"]/span/text()').extract()
        items["product_name"] = "".join(title).strip()
        items["product_platform"] = ",".join(map(lambda x: x.strip(), platform)).strip()
        items["product_sale_price"] = "".join(sale_price).strip()
        yield items

