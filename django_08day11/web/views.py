# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from web.models import Asset
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

def Add(request,name):#添加传入name作为hostname
    Asset.objects.create(hostname=name) #xx.objects django默认类的实例，提供了get、put等方法
    return HttpResponse('ok')

def Delete(request,id):#删除时，传入id即可
    Asset.objects.get(id=id).delete()
    return HttpResponse('ok')