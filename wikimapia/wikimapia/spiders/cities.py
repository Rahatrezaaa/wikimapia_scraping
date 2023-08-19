import scrapy

from ..items import WikimapiaItem

import json
# Opening JSON file
f = open('../states.json')
data = json.load(f)
urls=[]
for l in data:
    urls.append(l['link'])


class Wiki(scrapy.Spider):
    name='city'

    #start_urls=["https://wikimapia.org/country/India/Bihar/"]
    start_urls=urls

    def parse(self,response):

        items=WikimapiaItem()

        entry=response.css("#page-content a:nth-child(1)")

        city_texts=entry.css("::text").getall()
        city_links=entry.css("::attr(href)").getall()

        print("hffflasglyfsdkhjghdyfgytdrjstdytf")

        print("got citys names", len(city_links))

        for i in range(len(city_texts)) :

            items['name']=city_texts[i]
            items['link']=response.request.url+city_links[i]

            yield items
