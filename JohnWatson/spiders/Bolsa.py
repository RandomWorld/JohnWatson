import scrapy

class Bolsa(scrapy.Spider):
    name = "Bolsa"
    start_urls=["https://www.infobolsa.es/mercado-nacional/mercado-continuo"]


    def parse(self,response):
        Acciones =response.css("#instrumentListTable>table>tbody")
        for Accion in Acciones.css("tr"):
            yield {
                #'company':          Accion.css("td.name").css("a::text").getall()[0],
                'company':          Accion.css("td.name").css("a::text").get(),
                'Last'  :           float(Accion.css('td.price').css("td::text").getall()[0].replace("\r","").replace("\n","").replace(" ","").replace(",",".")),
                #Theoretically, it sjould NOT be price, it should be price.top but the name change
                'Path'  :           Accion.css("td.name").css("a").attrib["href"],                 
                'Variation' :       float(Accion.css('td.changeP').css("td::text").getall()[0].replace("\r","").replace("\n","").replace(" ","").replace(",",".")),
            }
            