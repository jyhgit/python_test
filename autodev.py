#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 14:59
# @Author  : jiayanhua
# @Site    : 
# @File    : autodev.py
# @Software: PyCharm Community Edition
#IPy
'''

from IPy import IP
#以不同格式展示
print(IP('192.168.0.0/24').strNormal(0))
print(IP('192.168.0.0/24').strNormal(1))
print(IP('192.168.0.0/24').strNormal(2))
print(IP('192.168.0.0/24').strNormal(3))
#多网格计算方法，ip段是否叠加
print IP('10.0.0.0/24')<IP('10.0.0.0/26')
print IP('192.168.1.100') in IP('192.168.1.0/24')
print IP('192.168.0.0/23').overlaps('192.168.1.0/24')
print IP('192.168.1.0/24').overlaps('192.168.2.0')
###version
print IP('10.0.0.0/8').version()
print IP('::1').version()

ip=IP('192.168.75.0/31')
print ip.len() #网段ip数量
for i in ip:#打印ip
    print (i)

ip1=IP('192.168.65.5')
print ip1.reverseNames() #ip反向地址
print ip1.iptype()
print ip1.strHex() #16进制
print ip1.strBin() #二进制

print(IP('192.168.1.0').make_net('255.255.252.0')) 
print(IP('192.168.1.0/255.255.248.0',make_net=True))
print(IP('192.168.1.0-192.168.1.255',make_net=True))

ip_s = raw_input('please enter you ip/net: ')
ips=IP(ip_s)
if ip_s.len() > 1:
    print ('net:%s' %ips.net())
    print ('netmask:%s' %ips.netmask())
    print ('broadcast:%s' %ips.broadcast())
    print ('reverse address:%s' %ips.reverseNames()[0])
    
'''
#DNS
## A 记录
import dns.resolver
domain = raw_input('please enter domain : ')
A = dns.resolver.query(domain,'A') #指定查A记录/NS/CNAME
for i in A.response.answer:
    for j in i.items:
        print j.address






