# -*- coding:utf-8 -*-
import re
import scrapy
from report_crawler.spiders.__Global_function import get_localtime
from report_crawler.spiders.__Global_variable import now_time, end_time


class JLU001_Spider(scrapy.Spider):
	name = 'JLU001'
	start_urls = ['http://ccst.jlu.edu.cn/?mod=info&act=list&id=67']
	domain = 'http://ccst.jlu.edu.cn/'

	def parse(self, response):
		messages = response.xpath("//div[@id='list']/ul/li")

		for i, message in enumerate(messages):
			# 置顶的通知会打乱顺序，必须要排除
			report_sign = message.xpath("font[@color='red']")
			if len(report_sign) != 0:
				continue

			report_name = message.xpath("a/@title").extract()[0]
			if re.search(u"报告|讲座", report_name) is None:
				continue

			report_time = get_localtime(message.xpath("span[@class='info_time']/text()").extract()[0].strip())
			if report_time > end_time:
				continue
			if report_time < now_time:
				return

			report_url = self.domain + message.xpath("a/@href").extract()[0]
			print report_url
			yield scrapy.Request(report_url, callback=self.parse_pages,
			                     meta={'link': report_url, 'number': i + 1, 'publication': report_time})

	def parse_pages(self, response):
		messages = response.xpath("//div[@class='readcontent']/p")

		return {'text': messages, 'number': response.meta['number'], 'organizer': u"吉林大学大学计算机科学与技术学院",
		        'faculty': self.name, 'link': response.meta['link'], 'publication': response.meta['publication'],
		        'location': u"东北:吉林省-长春市"}
