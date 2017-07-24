# -*- coding:utf-8 -*-
import re
import scrapy
from report_crawler.spiders.__Global_function import get_localtime
from report_crawler.spiders.__Global_variable import now_time, end_time


class NCU001_Spider(scrapy.Spider):
	name = 'NCU001'
	start_urls = ['http://ies.ncu.edu.cn/dwjl/xsdt/index.htm']
	domain = 'http://ies.ncu.edu.cn/dwjl/xsdt/'

	def parse(self, response):
		messages = response.xpath("//ul[@class='list']/li")

		for i, message in enumerate(messages):
			report_name = message.xpath(".//a/@title").extract()[0]
			report_name = re.sub(u"[\s\S]*(学术(报告|讲座)|题目)[：:.]", '', report_name) \
						if re.search(u"(学术(报告|讲座)|题目)[：:.]", report_name) is not None else report_name

			report_time = get_localtime(message.xpath("text()").extract()[0].strip().strip("[]"))
			if report_time > end_time:
				continue
			if report_time < now_time:
				return

			report_url = self.domain + message.xpath(".//a/@href").extract()[0]

			yield scrapy.Request(report_url, callback=self.parse_pages,
			                     meta={'link': report_url, 'number': i + 1, 'publication': report_time, 'title': report_name})

	def parse_pages(self, response):
		messages = response.xpath("//div[@class='font']")

		return {'text': messages, 'number': response.meta['number'], 'organizer': u'南昌大学信息工程学院',
		        'faculty': self.name, 'link': response.meta['link'], 'publication': response.meta['publication'],
		        'location': u"华东:江西省-南昌市", 'title': response.meta['title']}