# -*- coding:utf-8 -*-
import scrapy
from report_crawler.spiders.__Global_function import get_localtime
from report_crawler.spiders.__Global_variable import now_time, end_time


class SEU001_Spider(scrapy.Spider):
	name = 'SEU001'
	start_urls = ['http://cse.seu.edu.cn/CSE/UI/Notice/Notice.aspx?Notice_Type=1']
	domain = 'http://cse.seu.edu.cn/CSE/UI/Notice/'

	def parse(self, response):
		messages = response.xpath("//table[@class='datatable']/tr")

		for i, message in enumerate(messages[:len(messages) - 1]):
			report_name = message.xpath(".//a/@title").extract()[0]
			if u"讲座" not in report_name:
				continue

			report_time = get_localtime(message.xpath("td")[-1].xpath("span/text()").extract()[0])
			if report_time > end_time:
				continue
			if report_time < now_time:
				return

			report_url = self.domain + message.xpath(".//a/@href").extract()[0]
			yield scrapy.Request(report_url, callback=self.parse_pages,
			                     meta={'link': report_url, 'number': i + 1, 'publication': report_time})

	def parse_pages(self, response):
		messages = response.xpath("//div[@class='notice-content']")

		return {'text': messages, 'number': response.meta['number'], 'organizer': u'东南大学计算机科学与工程学院',
		        'faculty': self.name, 'link': response.meta['link'], 'publication': response.meta['publication'],
		        'location': u"华东:江苏省-南京市"}
