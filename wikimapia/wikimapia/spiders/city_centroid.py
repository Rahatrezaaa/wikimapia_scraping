import scrapy

from ..items import WikimapiaItem

import json
# Opening JSON file
f = open('../all_cities.json')
data = json.load(f)
urls=[]
for l in data:
    urls.append(l['link'])


class Wiki(scrapy.Spider):
    name='centroid'

    #start_urls=["https://wikimapia.org/country/India/Bihar/"]
    start_urls=urls

    def parse(self,response):

        items=WikimapiaItem()

        entry=response.css("li.active::text").get()

        items['name']=entry
        yield items