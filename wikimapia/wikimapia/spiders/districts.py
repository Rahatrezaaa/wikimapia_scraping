import scrapy

from ..items import WikimapiaItem

class Wiki(scrapy.Spider):
    name='dist'

    start_urls=["https://wikimapia.org/country/India/Bihar/"]

    def parse(self,response):

        items=WikimapiaItem()

        districts_text=response.css(".span8 li::text").getall()

        print("hffflasglyfsdkhjghdyfgytdrjstdytf")

        print("got states names", len(districts_text))

        for i in range(len(districts_text)) :

            items['name']=districts_text[i]
            
            yield items