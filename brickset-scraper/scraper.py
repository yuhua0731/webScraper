#!/usr/bin/env python3
import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

if __name__ == '__main__':
    print(f'simple scraper')

