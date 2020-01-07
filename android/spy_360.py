# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:30:11 2017
@author: GXW
used
"""

import re
import urllib
import os


# response=urllib.urlopen('http://zhushou.360.cn/list/index/cid/1?page=1')
# html=response.read()
# link_list=re.findall(r"(?<=&url=).*?apk",html)
# for url in link_list:
#    print url
class testClass:
    def __init__(self):
        self.urllist = []
        self.k = 1
        self.baseurl = 'http://zhushou.360.cn/list/index/cid/1?page='

    def geturl(self, pageindex):
        for i in range(1, pageindex + 1):
            self.urllist.append(self.baseurl + str(i))

    def spider(self):
        for i in range(len(self.urllist)):
            response = urllib.urlopen(self.urllist[0])
            html = response.read()
            link_list = re.findall(r"(?<=&url=).*?apk", html)
            for url in link_list:
                file_name = "%d.apk" % (self.k)
                self.k = self.k + 1
                file_path = os.path.join("/home/huu/Downloads/apk_360", file_name)
                urllib.urlretrieve(url, file_path)
            del self.urllist[0]
            print (i)

    def start(self):
        self.geturl(50)
        self.spider()


a = testClass()
a.start()