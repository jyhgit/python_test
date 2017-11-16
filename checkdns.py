#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 19:43
# @Author  : jiayanhua
# @Site    : 
# @File    : checkdns.py
# @Software: PyCharm Community Edition
#定义域名，
#解析域名获取ip,多个ip访问list中
#对ip进行http检测
import  dns.resolver
import httplib
import os

iplist = []
appdomain = "www.qq.com"

def get_doaminip(domain=""):
    try:
        ips=dns.resolver.query(domain,'A')
    except Exception,e:
        print " resolver is error:"+ str(e)
        return
    for i in ips.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True
def checkip(ip):
    checkurl = ip + ":80"
    #print checkurl
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(checkurl)
    try:
        conn.request("GET","/",headers={"Host":appdomain}) #发起url请求
        r = conn.getresponse()
        getcontent = r.read(15)
        #print getcontent
    finally:
        if getcontent == "<!DOCTYPE html>":
            print ip +"[ok]"
        else:
            print ip + "[error]"
if __name__ == "__main__":
    #print iplist
    if get_doaminip(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns reslove is error"