# -*- coding:utf-8 -*-
import scrapy
from report_crawler.spiders.__Global_function import get_localtime
from report_crawler.spiders.__Global_variable import now_time, end_time


class CSU001_Spider(scrapy.Spider):
	name = 'CSU001'
	start_urls = ['http://sise.csu.edu.cn/index/xsxx.htm']
	domain = 'http://sise.csu.edu.cn/'

	def parse(self, response):
		messages = response.xpath("//div[@class='article-list-right']/div[@class='article-list-right-li new-article']")

		for i, message in enumerate(messages):
			report_time = get_localtime(message.xpath(".//div[@class='article-list-left-li-r']/text()").extract()[0])
			if report_time > end_time:
				continue
			if report_time < now_time:
				return

			report_url = self.domain + message.xpath(".//a/@href").extract()[0][3:]
			yield scrapy.Request(report_url, callback=self.parse_pages,
			                     meta={'link': report_url, 'number': i + 1, 'publication': report_time})

	def parse_pages(self, response):
		messages = response.xpath("//div[@class='article-right-middle']")

		return {'text': messages, 'number': response.meta['number'], 'organizer': u"中南大学大学信息科学与工程学院",
		        'faculty': self.name, 'link': response.meta['link'], 'publication': response.meta['publication'],
		        'location': u"华中:湖南省-长沙市"}
