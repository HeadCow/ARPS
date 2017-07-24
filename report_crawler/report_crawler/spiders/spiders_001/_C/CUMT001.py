# -*- coding:utf-8 -*-
import re
import scrapy
from report_crawler.spiders.__Global_function import get_localtime
from report_crawler.spiders.__Global_variable import now_time, end_time


class CUMT001_Spider(scrapy.Spider):
	name = 'CUMT001'
	start_urls = ['http://cs.cumt.edu.cn/list.php?classname=%E7%A7%91%E7%A0%94%E7%A0%94%E7%A9%B6%E7%94%9F&p=1']
	domain = 'http://cs.cumt.edu.cn/'

	def parse(self, response):
		messages = response.xpath("//div[@class='articlelist']/table/tr")

		for i, message in enumerate(messages):
			report_name = message.xpath(".//a/@title").extract()[0]
			if re.search(u"学术(报告|讲座)", report_name) is None:
				continue

			report_time = get_localtime(message.xpath("td")[-1].xpath('.//text()').extract()[0].strip())
			if report_time > end_time:
				continue
			if report_time < now_time:
				return

			report_url = self.domain + message.xpath(".//a/@href").extract()[0]
			yield scrapy.Request(report_url, callback=self.parse_pages,
			                     meta={'link': report_url, 'number': i + 1, 'publication': report_time})

		# 一页的报告太少，有多出一页的可能
		next_url = ''
		number_list = response.xpath("//div[@class='articlelist']/a")
		for i, number in enumerate(number_list):
			if re.search(u"下一页", number.xpath("text()").extract()[0]) is None:
				continue
			next_url = self.domain + number_list[i].xpath("@href").extract()[0]

		if next_url == '':
			return
		yield scrapy.Request(next_url, callback=self.parse)


	def parse_pages(self, response):
		messages = response.xpath("//div[@class='articleContent']/font")

		return {'text': messages, 'number': response.meta['number'], 'organizer': u'中国矿业大学计算机科学与技术学院',
		        'faculty': self.name, 'link': response.meta['link'], 'publication': response.meta['publication'],
		        'location': u"华东:江苏省-徐州市"}
