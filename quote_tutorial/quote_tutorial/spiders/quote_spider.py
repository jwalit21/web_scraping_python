import scrapy
from scrapy.http import FormRequest
from ..items import QuoteTutorialItem
from scrapy.utils.response import open_in_browser
class QuoteSpider(scrapy.Spider):
    
    name = 'quote'
    page_number = 2   #for pagination
    start_urls = [
        
        'http://quotes.toscrape.com/login'       #for next button url nevigation
    ]
    
    def parse(self,response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'admin',
            'password' : 'admin'
        },callback=self.start_crawling)
    
    def start_crawling(self,response):
        open_in_browser(response)