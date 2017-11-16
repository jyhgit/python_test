#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9 0:29
# @Author  : jiayanhua
# @Site    : 
# @File    : config.py
# @Software: PyCharm Community Edition

def login():
    return 'login'
def logout():
    return 'logout'

url = (
    ('/login/',login),
    ('/logout',logout),
)