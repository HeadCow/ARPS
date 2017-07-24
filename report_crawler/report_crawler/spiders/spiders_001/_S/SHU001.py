# -*- coding:utf-8 -*-
import re
import scrapy
from report_crawler.spiders.__Global_function import get_localtime
from report_crawler.spiders.__Global_variable import now_time, end_time

class SHU001_Spider(scrapy.Spider):
	name = 'SHU001'
	start_urls = ['http://cs.shu.edu.cn/Default.aspx?tabid=556']
	domain = 'http://cs.shu.edu.cn/'

	def parse(self, response):
		messages = response.xpath("//div[@id='dnn_ctr1319_ModuleContent']/table")[0].xpath("tr")

		for i, messages in enumerate(messages[:-1]):
			report_time = get_localtime(messages.xpath(".//td[@align='right']/span/text()").extract()[0].strip())
			if report_time > end_time:
				continue
			if report_time < now_time:
				return

			report_name = re.findall(u"学术报告[\d]*[：:-]([\s\S]*)", messages.xpath(".//a/@title").extract()[0])[0].strip()

			report_url = self.domain + messages.xpath(".//a/@href").extract()[0][1:]

			yield scrapy.Request(report_url, callback=self.parse_pages,
			                     meta={'link': report_url, 'number': i + 1, 'publication': report_time, 'title': report_name})

	def parse_pages(self, response):
		messages = response.xpath("//span[@id='dnn_ctr1319_ArticleDetails_ctl00_lblArticle']")

		return {'text': messages, 'number': response.meta['number'], 'organizer': u'上海大学计算机科学与工程学院',
		        'faculty': self.name, 'link': response.meta['link'], 'publication': response.meta['publication'],
		        'location': u"华东:上海市", 'title': response.meta['title']}

