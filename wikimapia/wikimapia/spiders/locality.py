import scrapy
import re
from ..items import WikimapiaItem,locality_item

class Wiki(scrapy.Spider):
    name='locality'

    start_urls=["http://wikimapia.org/9280998/te/SUPADIBAGICHA"]
    
    def parse(self,response):

        items=locality_item()

        loc_link=response.request.url
        items['link']=loc_link
        name=loc_link.split("/")[-1]
        items['name']=name

        #items['hierarchy']=response.css("#placeinfo-locationtree a::attr(href)").getall()
        items['hierarchy']=response.css(".placeinfo-row.hidden a::text").getall()
        items['tag']=response.css(".category ::text").get()

        txt=response.css("script")[1].get()
        search=re.search("lat .+",txt)
        lat=float(txt[search.start()+6:search.end()-1])

        items['lat']=lat

        search=re.search("lon .+",txt)
        lng=float(txt[search.start()+6:search.end()-1])
        items['lng']=lng
    

        #items["coordinates"]=response.css(".nested-objects~ div+ div::text").get().strip()


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


