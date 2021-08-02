# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class CleanProductVariantsPipeline:
    def process_item(self, snus, spider):
        for i in range(0, len(snus['productVariants'])):
            snus['productVariants'][i] = snus['productVariants'][i].strip(" \n")
        snus['productVariants'] = [x for x in snus['productVariants'] if x != '' and x != '\n']
        return snus

class CleanProductVariantsPricePipeline:
    def process_item(self, snus, spider):
        for i in range(0, len(snus['productVariantsPrices'])):
            snus['productVariantsPrices'][i] = snus['productVariantsPrices'][i].strip(" \n")
        #snus['productVariants'] = [x for x in snus['productVariants'] if x != '' and x != '\n']
        return snus

