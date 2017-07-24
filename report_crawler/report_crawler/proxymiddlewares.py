# -*- coding: utf-8 -*-
import random, base64


class ProxyMiddleware(object):

    proxyList = [ \
        '121.193.143.249:80','112.126.65.193:80','122.96.59.104:82','115.29.98.139:9999','117.131.216.214:80','116.226.243.166:8118','101.81.22.21:8118','122.96.59.107:843'
        ]

    def process_request(self, request, spider):
        # Set the location of the proxy
        pro_adr = random.choice(self.proxyList)
        print("USE PROXY -> " + pro_adr)
        request.meta['proxy'] = "http://" + pro_adr
