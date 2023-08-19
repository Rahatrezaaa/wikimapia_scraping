import scrapy

from ..items import WikimapiaItem


import json
# Opening JSON file
f = open('../all_cities.json')
data = json.load(f)
urls=[]
for l in data:
    urls.append(l['link'])

print(urls)
class Wiki(scrapy.Spider):
    name='amarpur'

    page_number=50

    #start_urls=["https://wikimapia.org/country/India/Bihar/Amarpur/"]
    start_urls=urls

    def parse(self,response):

        items=WikimapiaItem()

        loc_texts=response.css(".linkslist a:nth-child(1)::text").getall()

        if len(loc_texts)==0:
            return 
        loc_links=response.css(".linkslist a:nth-child(1)::attr(href)").getall()
        links=[]
        for link in loc_links:
            if link[-1]!="/":
                links.append(link)


        print("hffflasglyfsdkhjghdyfgytdrjstdytf")

        print("got states names", len(loc_links))

        for i in range(len(links)) :

           
            items['name']=loc_texts[i]
            items['link']=links[i]

            yield items

        
        next_url=Wiki.start_urls[0][:-2:]+str(Wiki.page_number)+"/"

        #if Wiki.page_number<200:

        Wiki.page_number+=50

        yield response.follow(next_url,callback=self.parse)


        
        


