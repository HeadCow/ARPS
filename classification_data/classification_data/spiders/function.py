# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_title():
	title = []
	with open('/Users/jingyuanli/ARPS/classification_data/title.txt', 'r') as f:
		lines = f.readlines()
		for line in lines:
			title.append(line.strip())
	return title

print len(get_title())
