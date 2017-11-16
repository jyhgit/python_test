#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/12 10:28
# @Author  : jiayanhua
# @Site    : 
# @File    : Account.py
# @Software: PyCharm Community Edition
# 处理账号相关的
def login():
    #读取html文件
    #再与数据库中的账号密码进行比对，对数据库存、取用到model模块
    #返回给用户时用到view
    f = file('E:\example\djangotest\Template\Account\login.html')
    data = f.read()
    return data
    #return "login"

def loginout():
    return "loginout"

def changepasswd():
    return "changepassdd"

