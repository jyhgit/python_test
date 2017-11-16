# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def login():
    return "login"

def index(request):#django  固定格式，接受http请求
    return HttpResponse('index') #同上固定格式，返回http

def login(request):
    return HttpResponse('login')

def list(request,name,id):#传递参数与urls模板一致，多个需要按顺序
    print name,id
    return HttpResponse('list')