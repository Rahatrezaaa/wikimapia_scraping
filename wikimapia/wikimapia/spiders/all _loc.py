import scrapy
import re
from ..items import WikimapiaItem,locality_item

import json
# Opening JSON file
f = open('../all_cities.json')
data = json.load(f)
urls=[]

for l in data:
    urls.append(l['link'])

urls_to_scrape=urls[130:200]


class Wiki(scrapy.Spider):
    name='city_spider'

    #start_urls=["https://wikimapia.org/country/India/Assam/Abhayapuri/"]
    start_urls=urls_to_scrape

    def parse(self,response):

        items=WikimapiaItem()

        loc_texts=response.css(".linkslist a:nth-child(1)::text").getall()
        loc_links=response.css(".linkslist a:nth-child(1)::attr(href)").getall()
        links=[]

        for link in loc_links:
            if link[-1]!="/":
                links.append(link)

        for i in range(len(links)) :

            yield response.follow(links[i],callback=self.loc_parse)


        if response.css('a[rel="next"]::attr(href)').get() is not None:

            next_url='https://wikimapia.org'+response.css('a[rel="next"]::attr(href)').get()

            yield response.follow(next_url,callback=self.parse)



    def loc_parse(self,response):
        
        items=locality_item()

        loc_link=response.request.url
        items['link']=loc_link
        #name=loc_link.split("/")[-1]
        name=response.css("title::text").get()
        
        items['name']=name
        items['hierarchy']=response.css(".placeinfo-row.hidden a::text").getall()
        items['tag']=response.css(".category ::text").get()


        txt=response.css("script")[1].get()
        search=re.search("lat .+",txt)
        lat=float(txt[search.start()+6:search.end()-1])

        items['lat']=lat

        search=re.search("lon .+",txt)
        lng=float(txt[search.start()+6:search.end()-1])
        items['lng']=lng
    
        #coord=response.css(".nested-objects~ div+ div::text").get().strip()

        #if coord=='':
        #    coord=response.css(".wikipedia-link~ div+ div::text").get().strip()



        #items["coordinates"]=coord


        entries=response.css("#similar-places li")

        sim_places=[]

        for entry in entries:
            n=entry.css("a ::text").get()
            d=entry.css(".nearest-distance ::text").get()
            sim_places.append({"name":n,"distance":d})


        items['similar_places']=sim_places


        entries=response.css("#nearby-places li")
        near_places=[]

        for entry in entries:
            n=entry.css("a ::text").get()
            d=entry.css(".nearest-distance ::text").get()
            near_places.append({"name":n,"distance":d})


        items['nearby_places']=near_places

        yield items




        
        


