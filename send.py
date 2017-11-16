#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/15 21:36
# @Author  : jiayanhua
# @Site    : 
# @File    : send.py
# @Software: PyCharm Community Edition

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()