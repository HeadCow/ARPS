# -*- coding: utf-8 -*-
import re

def get_information(text, faculty):
	messages = {}

	if faculty[-3:] == '001':
		messages = Parser(text)

	return messages


def sub_linefeed(text):
	sub_text = ''
	for line in text.splitlines():
		line = line.rstrip()
		if line != '':
			line += '\n'
		sub_text += line
	return sub_text


def masterFilter(text):
	re.sub(u"((((讲座|主讲|报告|演讲|讲)(者|人|师|专家|嘉宾)|个人)|(教授|院士|博士))(及其)*(简介|介绍|简历)([ (（](Biography|Bio|Short-Biography|Short bio))*|简历|Biography|Bio|Short-Biography|Short bio)[）) ]*[\s\S]*", '', text)
	re.sub(u"(((报告|讲座|内容)*(主要)*(内容|(摘|提|概)要)(简介|介绍){0,1}|(报告|讲座|内容)(简介|介绍))([ (（]Abstract)*|Abstract)[）) ]*[\s\S]*", '', text)

	return text


# 匹配各种符号(包括&nbsp;): "((?![\u4e00-\u9fa5])[\W])*"
def Filter(text, ab_sign=0):
	# title
	if re.search(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座|演((?![\u4e00-\u9fa5])[\W])*讲)*(主((?![\u4e00-\u9fa5])[\W])*题|题((?![\u4e00-\u9fa5])[\W])*目|标((?![\u4e00-\u9fa5])[\W])*题))([ (（](Title|Topic))*|Title|Topic)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座|演((?![\u4e00-\u9fa5])[\W])*讲)*(主((?![\u4e00-\u9fa5])[\W])*题|题((?![\u4e00-\u9fa5])[\W])*目|标((?![\u4e00-\u9fa5])[\W])*题))([ (（](Title|Topic))*|Title|Topic)[）) ]*[：:.]+[\s\S]*", '', text)

	# time
	if re.search(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座)*(日期及)*(时((?![\u4e00-\u9fa5])[\W])*间|日((?![\u4e00-\u9fa5])[\W])*期))([ (（]Time)*|Time)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座)*(日期及)*(时((?![\u4e00-\u9fa5])[\W])*间|日((?![\u4e00-\u9fa5])[\W])*期))([ (（]Time)*|Time)[）) ]*[：:.]+[\s\S]*", '', text)

	# address
	if re.search(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座)*地((?![\u4e00-\u9fa5])[\W])*点)([ (（](Address|Venue|Location|Meeting Room|Place))*|Address|Venue|Location|Meeting Room|Place)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座)*地((?![\u4e00-\u9fa5])[\W])*点)([ (（](Address|Venue|Location|Meeting Room|Place))*|Address|Venue|Location|Meeting Room|Place)[）) ]*[：:.]+[\s\S]*", '', text)

	# speaker
	if re.search(u"(((讲((?![\u4e00-\u9fa5])[\W])*座|讲((?![\u4e00-\u9fa5])[\W])*授|演((?![\u4e00-\u9fa5])[\W])*讲|报((?![\u4e00-\u9fa5])[\W])*告|主((?![\u4e00-\u9fa5])[\W])*讲)((?![\u4e00-\u9fa5])[\W])*(人|专((?![\u4e00-\u9fa5])[\W])*家|嘉((?![\u4e00-\u9fa5])[\W])*宾)|讲((?![\u4e00-\u9fa5])[\W])*(师|者)|主((?![\u4e00-\u9fa5])[\W])*讲)([ (（]Speaker)*|Speaker)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"(((讲((?![\u4e00-\u9fa5])[\W])*座|讲((?![\u4e00-\u9fa5])[\W])*授|演((?![\u4e00-\u9fa5])[\W])*讲|报((?![\u4e00-\u9fa5])[\W])*告|主((?![\u4e00-\u9fa5])[\W])*讲)((?![\u4e00-\u9fa5])[\W])*(人|专((?![\u4e00-\u9fa5])[\W])*家|嘉((?![\u4e00-\u9fa5])[\W])*宾)|讲((?![\u4e00-\u9fa5])[\W])*(师|者)|主((?![\u4e00-\u9fa5])[\W])*讲)([ (（]Speaker)*|Speaker)[）) ]*[：:.]+[\s\S]*", '', text)

	# abstract
	if re.search(u"(((报告|讲座|内容)*(主要)*(内容|(摘|提|概)要)(简介|介绍){0,1}|(报告|讲座|内容)(简介|介绍))([ (（]Abstract)*|Abstract)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"(((报告|讲座|内容)*(主要)*(内容|(摘|提|概)要)(简介|介绍){0,1}|(报告|讲座|内容)(简介|介绍))([ (（]Abstract)*|Abstract)[）) ]*[：:.]+[\s\S]*", '', text)

	# biography
	if re.search(u"((((讲座|主讲|报告|演讲|讲)(者|人|师|专家|嘉宾)|个人)|.*?(教授|院士|博士))(及其)*(简介|介绍|简历)([ (（](Biography|Bio|Short-Biography|Short bio))*|简历|Biography|Bio|Short-Biography|Short bio)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"((((讲座|主讲|报告|演讲|讲)(者|人|师|专家|嘉宾)|个人)|.*?(教授|院士|博士))(及其)*(简介|介绍|简历)([ (（](Biography|Bio|Short-Biography|Short bio))*|简历|Biography|Bio|Short-Biography|Short bio)[）) ]*[：:.]+[\s\S]*", '', text)

	# chairman
	if re.search(u"主((?![\u4e00-\u9fa5])[\W])*持((?![\u4e00-\u9fa5])[\W])*(人)*([ (（]Chair)*[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"主((?![\u4e00-\u9fa5])[\W])*持((?![\u4e00-\u9fa5])[\W])*(人)*([ (（]Chair)*[）) ]*[：:.]+[\s\S]*", '', text)

	# invitee
	if re.search(u"邀((?![\u4e00-\u9fa5])[\W])*请((?![\u4e00-\u9fa5])[\W])*人([ (（]Invitee)*[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"邀((?![\u4e00-\u9fa5])[\W])*请((?![\u4e00-\u9fa5])[\W])*人([ (（]Invitee)*[）) ]*[：:.]+[\s\S]*", '', text)

	# others
	if re.search(u"欢迎(各位|广大|全校)", text) is not None:
		text = re.sub(u"欢迎(各位|广大|全校)[\s\S]*", '', text)
	if re.search(u"报((?![\u4e00-\u9fa5])[\W])*告((?![\u4e00-\u9fa5])[\W])*([一二三四五]|[\d])[ ]*[：:.]*", text) is not None:
		text = re.sub(u"报[ ]*告[ ]*([一二三四五]|[\d])[ ]*[：:.]*[\s\S]*", '', text)
	if re.search(u"(查看次数|点击)[：:.]", text) is not None:
		text = re.sub(u"(查看次数|点击)[：:.][\s\S]*", '', text)
	if re.search(u"附件下载[：:.]", text) is not None:
		text = re.sub(u"附件下载[：:.][\s\S]*", '', text)
	if re.search(u"(主办|讲座|报告|演讲)(人)*(单位|企业)[：:.]", text) is not None:
		text = re.sub(u"(主办|讲座|报告|演讲)(人)*(单位|企业)[：:.][\s\S]*", '', text)
	if re.search(u"[一二三四五六七八九][、.]", text) is not None:
		text = re.sub(u"[一二三四五六七八九][、.][\s\S]*", '', text)
	if re.search(u"请我院相关[\s\S]*", text) is not None:
		text = re.sub(u"请我院相关[\s\S]*", '', text)

	if ab_sign == 0:
		text = masterFilter(text)

	return text


def Parser(text):
	text = text.decode('utf-8')
	messages = {}

	# title
	title_pattern = re.compile(u"(?:(?:(?:报(?:(?![\u4e00-\u9fa5])[\W])*告|讲(?:(?![\u4e00-\u9fa5])[\W])*座|演(?:(?![\u4e00-\u9fa5])[\W])*讲)*(?:主(?:(?![\u4e00-\u9fa5])[\W])*题|题(?:(?![\u4e00-\u9fa5])[\W])*目|标(?:(?![\u4e00-\u9fa5])[\W])*题))|Title|Topic)[）) ]*[：:.]+([\s\S]*)", re.S)
	messages['title'] = re.findall(title_pattern, text)
	if len(messages['title']) == 1:
		messages['title'] = messages['title'][0].strip()
	else:
		messages['title'] = ''
	messages['title'] = Filter(messages['title'], 0)

	# time
	time_pattern = re.compile(u"(?:(?:(?:报(?:(?![\u4e00-\u9fa5])[\W])*告|讲(?:(?![\u4e00-\u9fa5])[\W])*座)*(?:时(?:(?![\u4e00-\u9fa5])[\W])*间|日(?:(?![\u4e00-\u9fa5])[\W])*期))|Time)[）) ]*[：:.]+([\s\S]*)", re.S)
	messages['time'] = re.findall(time_pattern, text)
	if len(messages['time']) == 1:
		messages['time'] = messages['time'][0].strip()
	else:
		messages['time'] = ''
	messages['time'] = re.sub(u"[?!@#$&]", ' ', Filter(messages['time'], 0))

	# address
	address_pattern = re.compile(u"(?:(?:(?:报(?:(?![\u4e00-\u9fa5])[\W])*告|讲(?:(?![\u4e00-\u9fa5])[\W])*座){0,1}地(?:(?![\u4e00-\u9fa5])[\W])*点)|Address|Venue|Location|Meeting Room|Place)[）) ]*[：:.]+([\s\S]*)", re.S)
	messages['address'] = re.findall(address_pattern, text)
	if len(messages['address']) == 1:
		messages['address'] = messages['address'][0].strip()
	else:
		messages['address'] = ''
	messages['address'] = re.sub(u"[?!@#$&]", ' ', Filter(messages['address'], 0))

	# speaker
	speaker_pattern = re.compile(u"(?:(?:讲(?:(?![\u4e00-\u9fa5])[\W])*座|讲(?:(?![\u4e00-\u9fa5])[\W])*授|演(?:(?![\u4e00-\u9fa5])[\W])*讲|报(?:(?![\u4e00-\u9fa5])[\W])*告|主(?:(?![\u4e00-\u9fa5])[\W])*讲)[ ]*(?:人|专(?:(?![\u4e00-\u9fa5])[\W])*家|嘉(?:(?![\u4e00-\u9fa5])[\W])*宾)|讲(?:(?![\u4e00-\u9fa5])[\W])*(?:师|者)|主(?:(?![\u4e00-\u9fa5])[\W])*讲|Speaker)[）) ]*[：:.]+([\s\S]*)", re.S)
	messages['speaker'] = re.findall(speaker_pattern, text)
	if len(messages['speaker']) == 1:
		messages['speaker'] = messages['speaker'][0].strip()
	else:
		messages['speaker'] = ''
	messages['speaker'] = re.sub(u"[?!@#$&]", ' ', Filter(messages['speaker'], 0))

	# abstract
	abstract_pattern = re.compile(u"(?:(?:报告|讲座|内容)*(?:主要)*(?:内容|(?:摘|提|概)要)|(?:报告|讲座|内容)(?:简介|介绍)|Abstract)[）) ]*[：:.]+([\s\S]*)", re.S)
	messages['abstract'] = re.findall(abstract_pattern, text)
	if len(messages['abstract']) == 1:
		messages['abstract'] = sub_linefeed(messages['abstract'][0].strip())
	else:
		messages['abstract'] = ''
	messages['abstract'] = Filter(messages['abstract'], 1)

	# biography
	biography_pattern = re.compile(u"(?:(?:(?:(?:讲座|主讲|报告|演讲|讲)(?:者|人|师|专家|嘉宾)|个人)|.*?(?:教授|院士|博士))(?:及其)*(?:简介|介绍)|简历|Biography|Bio|Short-Biography|Short bio)[）) ]*[：:.]+([\s\S]*)", re.S)
	messages['biography'] = re.findall(biography_pattern, text)
	if len(messages['biography']) == 1:
		messages['biography'] = sub_linefeed(messages['biography'][0].strip())
	else:
		messages['biography'] = ''
	messages['biography'] = Filter(messages['biography'], 1)

	# If speaker is not exist, we could get it from the biography.
	if messages['speaker'] == '':
		speakerFromBioChina = re.match(u"(.*?)(教授|副教授|博士|讲师|院士)", messages['biography'])
		messages['speaker'] = '' if speakerFromBioChina is None else speakerFromBioChina.group()
	if messages['speaker'] == '':
		speakerFromBioEng = re.match(u"([A-Z][a-zA-Z]*[ .]*)+", messages['biography'])
		messages['speaker'] = '' if speakerFromBioEng is None else speakerFromBioEng.group()
	if messages['speaker'] == '':
		speakerFromBioAll = re.search(u"(.*?)(教授|副教授|博士|讲师|院士)(及其)*(简介|介绍|简历)[：:.]+", text)
		messages['speaker'] = '' if speakerFromBioAll is None else re.sub(u"(及其)*(简介|介绍|简历)[：:.]+", '', speakerFromBioAll.group().strip())

	if re.search(u"教授|院士|学者|主管|经理|讲师|专家|研究员|主任|CEO|CTO|博士", messages['speaker']) is not None:
		messages['speaker'] = re.search(u"(.*?)(教授|院士|学者|主管|经理|讲师|专家|研究员|主任|CEO|CTO|博士)", messages['speaker']).group()
	elif re.search(u"[，,]", messages['speaker']) is not None:
		messages['speaker'] = re.search(u"(.*?)[，,]", messages['speaker']).group().strip('，,')

	# If biography and abstract is not exists, we should try again without colon.
	if messages['biography'] == '':
		biography_pattern = re.compile(u"(?:(?:(?:(?:讲座|主讲|报告|演讲|讲)(?:者|人|师|专家|嘉宾)|个人)|.*?(?:教授|院士|博士))(?:及其)*(?:简介|介绍)|简历|Biography|Bio|Short-Biography|Short bio)[）) ]*([\s\S]*)", re.S)
		messages['biography'] = re.findall(biography_pattern, text)
		if len(messages['biography']) == 1:
			messages['biography'] = sub_linefeed(messages['biography'][0].strip())
		else:
			messages['biography'] = ''
		messages['biography'] = Filter(messages['biography'], 1)

	if messages['abstract'] == '':
		abstract_pattern = re.compile(u"(?:(?:报告|讲座|内容)*(?:主要)*(?:内容|(?:摘|提|概)要)|(?:报告|讲座|内容)(?:简介|介绍)|Abstract)[）) ]*([\s\S]*)", re.S)
		messages['abstract'] = re.findall(abstract_pattern, text)
		if len(messages['abstract']) == 1:
			messages['abstract' \
			         ''] = sub_linefeed(messages['abstract'][0].strip())
		else:
			messages['abstract'] = ''
		messages['abstract'] = Filter(messages['abstract'], 1)

	return messages
