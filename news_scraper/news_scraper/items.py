# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# news_scraper/items.py
import scrapy

class NewsScraperItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    pubDate = scrapy.Field()
    description = scrapy.Field()
