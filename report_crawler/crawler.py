# -*- coding:utf-8 -*-
from __future__ import print_function

import os
import time
import shutil
import traceback
from report_crawler.spiders.__Global_function import get_localtime
from report_crawler.spiders.__Global_variable import REPORT_SAVEDIR

now_time = get_localtime(time.strftime("%Y-%m-%d", time.localtime()))

DATADIR = REPORT_SAVEDIR + '/' + str(now_time)


class Spider_starter(object):

	def crawl(self):
		self.X001()

	def run_spider(self, spider_name):
		dirname = REPORT_SAVEDIR + '/' + str(now_time) + '/' + spider_name[len(spider_name)-3:] + '/' + spider_name[0:len(spider_name)-3]
		# If the dir is exist, clear the dir(today)
		if os.path.exists(dirname):
			shutil.rmtree(dirname, True)
		# If one of the spiders has error, the print_exc() function will tell us which is criminal
		try:
			if not os.path.exists(DATADIR):
				os.makedirs(DATADIR)
			os.system('scrapy crawl ' + spider_name)
		except:
			traceback.print_exc()

	def X001(self):

		spider_list = {
			'B': ['BNU001', 'BUAA001'],
			'C': ['CSU001', 'CUMT001'],
			'E': ['ECNU001'],
			'H': ['HNU001'],
			'J': ['JLU001'],
			'N': ['NCU001', 'NKU001', 'NWSUAF001'],
			'P': ['PKU001'],
			'S': ['SCU001', 'SDU001', 'SEU001', 'SHU001', 'SUDA001', 'SWJTU001', 'SWU001', 'SYSU001'],
			'T': ['THU001', 'TYUT001'],
			'U': ['UESTC001'],
			'W': ['WHU001'],
			'Z': ['ZZU001']
		}

		for key in spider_list.keys():
			for spider in spider_list[key]:
				self.run_spider(spider)

if __name__ == '__main__':
	starter = Spider_starter()
	starter.crawl()
