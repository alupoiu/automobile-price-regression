import scrapy
from scrapy import Request

class AutoTraderSpider(scrapy.Spider):
    name = 'civics'
    allowed_domains =['autotrader.com']
    start_urls = ['https://www.autotrader.com/cars-for-sale/honda/civic/fremont-ca-94538?requestId=2281868035&searchRadius=0&marketExtension=include&isNewSearch=true&showAccelerateBanner=false&sortBy=relevance&numRecords=100&firstRecord=']

    def parse(self, response):

        listing_SELECTOR = 'div > div.inventory-listing'
        MODEL_SELECTOR = '.text-size-400::text'
        PRICE_SELECTOR = '.first-price::text'
        MILES_SELECTOR = '.item-card-specifications ::text'

        for listing in response.css(listing_SELECTOR):
            yield{
                'model': listing.css(MODEL_SELECTOR).get(),
                'price': listing.css(PRICE_SELECTOR).get(),
                'miles': listing.css(MILES_SELECTOR).get(),
            }

        next_page = response.css('ul.pagination > li > a > span::text')[-1].get()

        current_page = response.css('ul.pagination > li.active > a::text').get()
        if next_page == 'Next Page':
            yield Request(url=('https://www.autotrader.com/cars-for-sale/honda/civic/fremont-ca-94538?requestId=2281868035&searchRadius=0&marketExtension=include&isNewSearch=true&showAccelerateBanner=false&sortBy=relevance&numRecords=100&firstRecord='+str(int(current_page)*100)), callback=self.parse)
        else:
            yield{
                "data collected from": current_page+' pages'
            }
        
