#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/15 21:37
# @Author  : jiayanhua
# @Site    : 
# @File    : recive.py
# @Software: PyCharm Community Edition

# !/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()