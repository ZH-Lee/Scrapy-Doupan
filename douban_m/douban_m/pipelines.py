# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class DoubanMPipeline(object):
	def open_spider(self,spider):
		self.file = open('douban_movie.text','w',encoding='utf-8')
		print('open file')

	def process_item(self, item, spider):
		line  = json.dumps(dict(item),ensure_ascii=False) +'\n'
		self.file.write(line)
		#print(line)
		return item

	def close_spider(self,spider):
		self.file.close()
		print('close file')
