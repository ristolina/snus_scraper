# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SnusItem(scrapy.Item):
    # define the fields for your item here like:
    productName = scrapy.Field()
    productUrl = scrapy.Field()
    productPrice = scrapy.Field()
    productSite = scrapy.Field()
    productId = scrapy.Field()
    unitPrice = scrapy.Field()
    units = scrapy.Field()
    productVariants = scrapy.Field()
    productVariantsPrices = scrapy.Field()
    
