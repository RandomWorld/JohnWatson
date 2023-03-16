import scrapy


class NewFile(scrapy.Spider):
    name = "JohnWatson"
    start_urls=["https://www.jobs.ch/en/vacancies/?language-skill=en&language-skill=missing&publication-date=7&sort-by=date&term=risk"]


    def parse(self,response):
        JobOffers=response.css("article.Div-sc-1cpunnt-0")
        for Offer in JobOffers:
            yield{

                "title" : Offer.css("a").attrib["title"],
                "link"  : Offer.css("a").attrib["href"],
                "localitation"  : Offer.css("a").css("p.P-sc-hyu5hk-0::text").get()
            }