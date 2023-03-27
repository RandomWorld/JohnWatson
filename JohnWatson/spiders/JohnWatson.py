import scrapy


class NewFile(scrapy.Spider):
    name = "JohnWatson"
    start_urls=["https://www.jobs.ch/en/vacancies/?language-skill=en&language-skill=missing&publication-date=7&sort-by=date&term=risk"]
    
    
    def parse(self,response):
        LastPage = False
        JobOffers=response.css("article.Div-sc-1cpunnt-0")
        for Offer in JobOffers:
            yield{
                "title" : Offer.css("a").attrib["title"],
                "link"  : Offer.css("a").attrib["href"],
                "localitation"  : Offer.css("a").css("p.P-sc-hyu5hk-0::text").get()
            }
        next_page=response.css("a.Link__ExtendedRR6Link-sc-czsz28-1.ieOBrl.Link-sc-czsz28-2.*").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)    




