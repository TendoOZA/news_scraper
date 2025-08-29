# news_scraper/spiders/news_spider.py
import scrapy
from news_scraper.items import NewsScraperItem

class NewsSpider(scrapy.Spider):
    name = "news_spider"
    allowed_domains = ["cnn.com"]
    start_urls = ["http://rss.cnn.com/rss/cnn_topstories.rss"]

    def parse(self, response):
        for item in response.xpath('//item'):
            news_item = NewsScraperItem()
            news_item['title'] = item.xpath('title/text()').get()
            news_item['link'] = item.xpath('link/text()').get()
            news_item['pubDate'] = item.xpath('pubDate/text()').get()
            news_item['description'] = item.xpath('description/text()').get()
            yield news_item
