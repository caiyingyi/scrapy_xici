# -*- coding:utf-8 -*-
__author__ = 'Windows'

import scrapy
import requests #用于测试抓取过来的IP是否可用
from xici.items import XiciItem

class XiciSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["xicidaili.com",]

    def start_requests(self):
        urls = ["http://www.xicidaili.com/nn/1/",
            "http://www.xicidaili.com/nn/2",
            "http://www.xicidaili.com/nn/3",
            "http://www.xicidaili.com/nn/4",
            "http://www.xicidaili.com/nn/5",
            "http://www.xicidaili.com/nn/6",
            "http://www.xicidaili.com/nn/7",
            "http://www.xicidaili.com/nn/8",
            "http://www.xicidaili.com/nn/10",
            "http://www.xicidaili.com/nn/11",
            "http://www.xicidaili.com/nn/12",
            "http://www.xicidaili.com/nn/13",
            "http://www.xicidaili.com/nn/14",
            "http://www.xicidaili.com/nn/15",
            "http://www.xicidaili.com/nn/16",
            "http://www.xicidaili.com/nn/17",
            "http://www.xicidaili.com/nn/18",
            "http://www.xicidaili.com/nn/19",
            "http://www.xicidaili.com/nn/20",



              ]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)

    def parse(self,response):
        item = XiciItem()

        table = response.xpath("//table[@id='ip_list']")[0] #定位那个装满IP的大框
        trs = table.xpath("//tr")[1:]       #过滤掉第一行的标题栏  国家 IP地址 端口 服务器地址 是否匿名 类型 速度 连接时间 存活时间 验证时间
        for tr in trs:
            pagetest = "http://su.58.com/danbaobaoxiantouzi/"   #用于测试的网页
            ip = tr.xpath("td[2]/text()").extract()[0]
            port = tr.xpath("td[3]/text()").extract()[0]

            PROXY = "http://" + ip + ":" + port
            proxies = {
                    "http":PROXY
                }

            print u"待检验的ip和port：" +PROXY

            try:
                response = requests.get(pagetest,timeout=1,proxies=proxies)

                print (response.status_code)

                if response.status_code == 200:#判断返回的状态代码来判断IP是否可用

                    item['ip'] = ip
                    item['port'] = port

                    yield item

            except:
                print("connect failed!")