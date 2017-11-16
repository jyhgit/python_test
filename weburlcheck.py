#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 21:36
# @Author  : jiayanhua
# @Site    : 
# @File    : weburlcheck.py
# @Software: PyCharm Community Edition

import os
import sys
import time
import pycurl


URL = "http://www.baidu.com" #
c = pycurl.Curl() #创建url对象
c.setopt(pycurl.URL,URL) #定义请求URL常量
c.setopt(pycurl.CONNECTTIMEOUT,5) #定义http请求等待时间
c.setopt(pycurl.TIMEOUT,5) #请求超时时间
c.setopt(pycurl.NOPROGRESS,1) #屏蔽下载进度条
c.setopt(pycurl.FORBID_REUSE,1) #完成交互后强制断开
c.setopt(pycurl.MAXREDIRS,1) # 重定向最大1
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30) #dns缓存信息的时间为30
#wb格式打开文件，存储http头部及内容信息
indexfile = open(os.path.dirname(os.path.realpath(__file__)) + "/content.txt",'wb')

c.setopt(pycurl.WRITEHEADER,indexfile) #http header 写入文件
c.setopt(pycurl.WRITEDATA,indexfile) #http 内容写入文件

try:
    c.perform() #提交请求
except Exception,e:
    print "connect is error " + str(e)
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

#print all
print "HTTP状态码: %s" %(HTTP_CODE)
print "DNS解析时间: %.2f ms" %(NAMELOOKUP_TIME * 1000)
print "建立连接时间: %.2f ms" %(CONNECT_TIME * 1000)
print "准备传输时间: %.2f ms" %(PRETRANSFER_TIME * 1000)
print "开始传输时间: %.2f ms" %(STARTTRANSFER_TIME * 1000)
print "传输结束总时间: %.2f ms" %(TOTAL_TIME * 1000)
print "下载包数据大小: %d bytes/s" %(SIZE_DOWNLOAD)
print "HTTPhead 大小: %d bytes/s" %(HEADER_SIZE)
print "平均下载速度: %d bytes/s" %(SPEED_DOWNLOAD)

#关闭文件
indexfile.close()
c.close()






