# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class info(scrapy.Item):
    title= scrapy.Field()
    release_year= scrapy.Field()
    rating= scrapy.Field()