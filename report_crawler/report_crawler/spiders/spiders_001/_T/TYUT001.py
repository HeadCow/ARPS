# -*- coding:utf-8 -*-
import re
import scrapy
from report_crawler.spiders.__Global_function import get_localtime
from report_crawler.spiders.__Global_variable import now_time, end_time

class TYUT001_Spider(scrapy.Spider):
	name = "TYUT001"
	start_urls = ['http://www.tyut.edu.cn/ccst/news_more.asp?lm=&lm2=74']
	domain = 'http://www.tyut.edu.cn/ccst/'

	def parse(self, response):
		messages = response.xpath("//div[@id='list']")

		for i, message in enumerate(messages):
			report_name = message.xpath(".//a/font/text()").extract()[0]
			if re.search(u"报告|讲座", report_name) is None:
				continue

			# 该网站格式是年月日，将所有中文换成'-'
			report_time = get_localtime(re.sub(u"[\u4e00-\u9fa5]", '-', message.xpath(".//div[@style='float:right']/font/text()").extract()[0].strip().strip('()')).strip('-'))
			if report_time > end_time:
				continue
			if report_time < now_time:
				return

			report_url = self.domain + message.xpath(".//a/@href").extract()[0]
			yield scrapy.Request(report_url, callback=self.parse_pages,
			                     meta={'link': report_url, 'number': i + 1, 'publication': report_time})

	def parse_pages(self, response):
		messages = [response.xpath("//table[@style='width: 95%']/tr/td/font/tr")[1]]

		return {'text': messages, 'number': response.meta['number'], 'organizer': u"太原理工大学大学计算机科学与技术学院",
		        'faculty': self.name, 'link': response.meta['link'], 'publication': response.meta['publication'],
		        'location': u"华北:山西省-太原市"}
