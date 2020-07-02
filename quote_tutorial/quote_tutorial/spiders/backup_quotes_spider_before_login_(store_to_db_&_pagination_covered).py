import scrapy
from ..items import QuoteTutorialItem
class QuoteSpider(scrapy.Spider):
    
    name = 'quote'
    page_number = 2   #for pagination
    start_urls = [
        
        #'http://quotes.toscrape.com/'       #for next button url nevigation
        'http://quotes.toscrape.com/page/1'  #for pagination
    ]
    
    def parse(self,response):
        
        items = QuoteTutorialItem()
        
        title = response.css('title::text').extract()
        quotes_x = response.xpath("//span[@class='text']/text()").extract()
        quote = response.css('div span.text::text')[1].extract()
        next_url = response.css("li.next a").xpath("@href").extract()
        urls = response.css("a").xpath("@href").extract()
        all_quote_data = response.css("div.quote")
        yield { 'titletext' : title, 'quotes': quote ,'quotes_x': quotes_x, 'next_url': next_url , 'urls': urls }
        for quotes in all_quote_data:
            quote_title = quotes.css("span.text::text").extract()
            authors = quotes.css("span small.author::text").extract()
            tag = quotes.css("div a.tag::text").extract()
            items['quote_title'] = quote_title
            items['author'] = authors
            items['tag'] = tag
            yield items
        
        #next_page = response.css("li.next a::attr(href)").get()                             #for next button url nevigation
        next_page = 'http://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'  #for pagination

        
        if(next_page):
            QuoteSpider.page_number += 1                                                     #for pagination
            yield response.follow(next_page, callback = self.parse)
            
        
        #scrapy crawl quote -o items.json/csv/xml