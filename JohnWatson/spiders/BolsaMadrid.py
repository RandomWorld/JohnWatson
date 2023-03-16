import scrapy
from scrapy.crawler import CrawlerProcess
#from scrapy.selector import HtmlXPathSelector




class BolsaMadrid(scrapy.Spider):
    name = "BolsaMadrid"
    start_urls=["https://www.infobolsa.es/mercado-nacional/mercado-continuo"]


    def parse(self,response):
        #Acciones=response.css("table")
        Ac =response.css("#instrumentListTable > table>tbody")
        #Acciones= response.xpath('//*[@id="root"]/div[3]/table')
        iter=0
        Ac2 =response.css("#instrumentListTable>table>tbody>tr")
        rst=[Ac,Ac2]
        return rst        
        
        """
        for tr in response.css("#instrumentListTable>table>tbody>tr"):
            print(str(iter)+"-----" + str(tr.get()))
            iter= iter+1


        for Accion in Acciones:
            yield {
                'company':           Accion.xpath('a/text()').extract(),
                'person' :           Accion.xpath('a/text()').extract(),
                'industry' :         Accion.xpath('a/text()').extract(),
                'url' :              Accion.xpath('a/@href').extract()
                #"Name" : Accion.css("table.a").attrib["title"],
                #"link"  : Offer.css("a").attrib["href"],
                #"localitation"  : Offer.css("a").css("p.P-sc-hyu5hk-0::text").get()
            }
        """
     



class test():
    
    import httpx
    from bs4 import BeautifulSoup
    process = CrawlerProcess()
    start_urls="https://www.infobolsa.es/mercado-nacional/mercado-continuo"






