# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WikimapiaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link=scrapy.Field()
    

class locality_item(scrapy.Item):    
    link=scrapy.Field()
    name=scrapy.Field()
    hierarchy=scrapy.Field()
    tag=scrapy.Field()
    lat=scrapy.Field()
    lng=scrapy.Field()
    similar_places=scrapy.Field()
    nearby_places=scrapy.Field()