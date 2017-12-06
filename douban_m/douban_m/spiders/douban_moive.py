# -*- coding: utf-8 -*-
# Time : 2017-11-27
# Author : Lee

import scrapy
from pyquery import PyQuery
from ..items import DoubanMItem


class DoubanMoiveSpider(scrapy.Spider):
	name = 'douban_moive'
	allowed_domains = ['movie.douban.com']
	start_urls = ['https://movie.douban.com/review/best/']

	def parse(self, response):
		
		jpy = PyQuery(response.text)

		l = jpy('div.review-list.chart > div > div').items()

		for it in l:
			item = DoubanMItem()
			item['author'] = it('header > a.name').text()
			item['score'] = it('header > span').attr('title')
			item['time'] = it('header > span').text()
			item['url'] = it('div.main-bd > h2 > a').attr('href')
			item['zan'] = it('div.main-bd > div.action > a.action-btn.up > span').text()
			item['buzan'] = it('div.main-bd > div.action > a.action-btn.down > span').text()
			yield item
			
		next_page = jpy('span.next > a').attr('href')
		print(next_page)
		if next_page is not None:
			yield response.follow(next_page,callback = self.parse)
			
			



