from warnings import catch_warnings
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from snus_scraper.items import SnusItem
import json


class SnusbolagetSpider(CrawlSpider):
    name = 'snusbolaget'
    allowed_domains = ['snusbolaget.se']
    start_urls = ['http://snusbolaget.se/snus']
    #start_urls = ['https://www.snusbolaget.se/snus/VOLT-Frosted-Apple-Slim-Strong-All-White-Portion']

    rules = [Rule(LinkExtractor(allow=r'\/snus\/(?:\w*\-\w*\-\w*-)'), callback='parse_info', follow=True)]

    def parse_info(self, response):
        json_data = json.loads(response.xpath('//script[@type="application/ld+json"]/text()').get().strip())
        snus = SnusItem()
        snus['productName'] = json_data['name']
        snus['productUrl'] = response.url
        #snus['productPrice'] = json_data['offers']['price']
        snus['productPrice'] = response.xpath('//span[@class="price-label"]/text()').get()[1:-7]
        #snus['units'] = response.xpath('//span[@class="price-label"]/preceding-sibling::*/descendant::text()').get()
        snus['productSite'] = 'snusbolaget.se'
        snus['productId'] = json_data['sku']
        snus['productVariants'] = response.xpath('//div[not (contains(@class, "tab-pane"))]/div[@class="variants list"]/ul[@class="list-unstyled"]/li/text()').getall()
        snus['productVariantsPrices'] = response.xpath('//div[not (contains(@class, "tab-pane"))]/div[@class="variants list"]/ul[@class="list-unstyled"]//span[@class="pull-right  "]/text()').getall()
        
        #try:
        #    snus['units'] = int(snus['productId'].split('-')[1][:-1])
        #except IndexError:
        #    snus['units'] = 10
        #if snus['units']:
        #    snus['unitPrice'] = float(snus['productPrice']) / float(snus['units'])

        return snus
