"""
get all the cities by iterting through each of state and following with cities of each statses

"""
import scrapy

from ..items import WikimapiaItem

class Wiki(scrapy.Spider):
    name='wiki'

    start_urls=["https://wikimapia.org/country/India/"]

    def parse(self,response):

        items=WikimapiaItem()

        state_texts=response.css(".linkslist a::text").getall()
        state_links=response.css(".linkslist a::attr(href)").getall()

        print("hffflasglyfsdkhjghdyfgytdrjstdytf")

        print("got states names", len(state_links))

        for i in range(len(state_texts)) :

            items['name']=state_texts[i]
            items['link']=self.start_urls[0]+state_links[i]

            yield items

        
        for link in state_links:

            link=self.start_urls[0]+link

            print("ffdgffffffffffdggrre")

            yield response.follow(link,callback=self.parse)

    
        
        


