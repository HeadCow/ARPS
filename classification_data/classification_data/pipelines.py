# -*- coding:utf-8 -*-

import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

title_name = 'title.txt'
filename = 'computer.txt'


class ClassificationDataPipeline(object):
    def process_item(self, item, spider):

        if not item.has_key('title'):
            return
        if self.getAllTitle(item['title']) is False:
            return

        signs, bigSigns = self.getSign(item['sign_list'])
        if not signs or not bigSigns:
            return

        with open(title_name, 'a') as t:
            t.write(item['title'] + '\n')
        with open(filename, 'a') as f:
            f.write('***' + '\n' * 2)
            f.write('Title: ' + item['title'].strip() + '\n')
            f.write('Abstract: ' + item['abstract'] + '\n')
            f.write('Sign: ')
            for sign in signs:
                f.write(sign + ' ')
            f.write('\nBigSign: ')
            for bigSign in bigSigns:
                f.write(str(bigSign) + ' ')
            f.write('\n' * 2)

    def getAllTitle(self, title):
        with open('title.txt', 'r') as f:
            for paper_title in f.readlines():
                if title.strip() == paper_title:
                    return False
            f.close()
        return True

    def getSign(self, sign_list):
        signs = {}
        bigSigns = {}
        for sign in sign_list:
            sign = sign.decode("utf-8")
            if re.search(u"自然(.*?)语言(.*?)处理|计算机(.*?)视觉|模式识别|聚类|(增强|强化|迁移|深度|机器)(.*?)学习|语音(.*?)识别|情感(.*?)计算|生物(.*?)信息", sign) is not None:
                signs['机器学习'] = 1
            if re.search(u"(数据|Web|文本)(.*?)挖掘|社会(.*?)计算|知识(.*?)(图谱|发现)", sign) is not None:
                signs['数据挖掘'] = 1
            if re.search(u"(信息|智能)(.*?)检索", sign) is not None:
                signs['信息检索'] = 1
            if re.search(u"人机(.*?)交互|(虚拟|增强)现实", sign) is not None:
                signs['人机交互'] = 1
            if re.search(u"云", sign) is not None:
                signs['云计算'] = 1

            if re.search(u"物联网|车(.*?)联网", sign) is not None:
                signs['物联网'] = 1
            if re.search(u"嵌入式|单片机|RFID|传感器|ARM", sign) is not None:
                signs['嵌入式'] = 1
            if re.search(u"并行|分布式", sign) is not None:
                signs['并行与分布式设计'] = 1

            if re.search(u"计算机(.*?)网络|(信息|网络)(.*?)安全|路由器|IPv(4|6)|密码|加密", sign) is not None:
                signs['网络与信息安全'] = 1
            if re.search(u"互联网", sign) is not None:
                signs['互联网'] = 1

            if re.search(u"图像", sign) is not None:
                signs['图像处理'] = 1
            if re.search(u"多媒体", sign) is not None:
                signs['多媒体技术'] = 1
            if re.search(u"图形学", sign) is not None:
                signs['计算机图形学'] = 1

            if re.search(u"数据库", sign) is not None:
                signs['数据库设计'] = 1
            if re.search(u"编译", sign) is not None:
                signs['编译技术'] = 1
            if re.search(u"操作系统", sign) is not None:
                signs['操作系统'] = 1
            if re.search(u"计算机(.*?)辅助设计|CAD", sign) is not None:
                signs['计算机辅助设计'] = 1
            if re.search(u"安卓|Android|IOS|JAVA|C#", sign) is not None:
                signs['软件设计与研究'] = 1

            if re.search(u"应用", sign) is not None:
                signs['实际应用'] = 1

        if signs.has_key('机器学习') or signs.has_key('数据挖掘') or signs.has_key('信息检索') or signs.has_key('人机交互') or signs.has_key('云计算'):
            bigSigns['0'] = 1
        if signs.has_key('物联网') or signs.has_key('嵌入式') or signs.has_key('并行与分布式设计'):
            bigSigns['1'] = 1
        if signs.has_key('网络与信息安全') or signs.has_key('互联网'):
            bigSigns['2'] = 1
        if signs.has_key('图像处理') or signs.has_key('多媒体技术') or signs.has_key('计算机图形学'):
            bigSigns['3'] = 1
        if signs.has_key('数据库设计') or signs.has_key('编译技术') or signs.has_key('操作系统') or signs.has_key('计算机辅助设计') or signs.has_key('软件设计与研究'):
            bigSigns['4'] = 1
        if signs.has_key('实际应用'):
            bigSigns['5'] = 1

        return signs, bigSigns
