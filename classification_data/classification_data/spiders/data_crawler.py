# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
from function import get_title

key_word = '软件开发'
start_year, end_year = 2014, 2017
all_name = get_title()
# all_name = []
class Data_Spider(scrapy.Spider):
	name = 'Crawler'
	start_urls = ['http://s.wanfangdata.com.cn/Paper.aspx?q=关键字%3a{}+日期%3a{}-{}+分类号%3a"TP3*"&f=subjectCatagory&p=1'.format(key_word, start_year, end_year)]

	def parse(self, response):
		messages = response.xpath("//div[@class='record-item-list']/div")

		# paper list
		for message in messages:
			paper_url = message.xpath(".//div[@class='record-title']/a[@class='title']/@href").extract()[0]
			sign_list = message.xpath(".//div[@class='record-keyword']/span/text()").extract()
			paper_name = self.get_name(message.xpath(".//div[@class='record-title']/a[@class='title']"))

			if paper_name in all_name:
				continue
			yield scrapy.Request(paper_url, callback=self.parse_pages, meta={'sign_list': sign_list})
		now_number = int(response.xpath("//p[@class='pager']/strong/text()").extract()[0])
		last_number = int(response.xpath("//p[@class='pager']/span/text()").extract()[0].split('/')[1])

		if now_number == last_number:
			return
		next_url = 'http://s.wanfangdata.com.cn/Paper.aspx?q=关键字%3a{}+日期%3a{}-{}+分类号%3a"TP3*"&f=subjectCatagory&p={}'.format(key_word, start_year, end_year, now_number + 1)

		yield scrapy.Request(next_url, callback=self.parse)

	def parse_pages(self, response):
		paper_name = response.xpath("//h1/text()").extract()[0].strip()
		abstract = response.xpath("//div[@class='row clear fl']/div[@class='text']/text()")
		abstract = response.xpath("//div[@class='row clear zh']/div[@class='text']/text()").extract()[0].strip() if len(abstract) == 0 else abstract.extract()[0].strip()

		all_messages = {'title': paper_name, 'abstract': abstract, 'sign_list': response.meta['sign_list']}

		return all_messages

	def get_name(self, message):
		texts = ''
		text_list = message.xpath(".//text()").extract()
		for text in text_list:
			texts += text.strip()
		return texts
