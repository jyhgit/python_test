# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from web.models import Asset
#from     django.db.models.manager.Manager import *

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
    #print type(Asset.objects) #打印引用方法出处
    #django.db.models.manager.Manager #对数据库的增删改查
    return HttpResponse('ok')

def Delete(request,id):#删除时，传入id即可
    Asset.objects.get(id=id).delete()
    return HttpResponse('ok')

def Update(request,id,hostname): #更新数据库
    #更新单条数据
    '''
    obj = Asset.objects.get(id=id)
    obj.hostname = hostname
    obj.save()
    '''
    Asset.objects.filter(id__gt=id),update(hostname=hostname) #批量修改大于指定id的hostnme全部修改
    return HttpResponse('ok')

def Get(request,hostname):
    assetlist = Asset.objects.filter(hostname__contains=hostname)
    #for item in assetlist:#循环列出id
    #    print item.id
    #print assetlist

    #alldata = Asset.objects.all() #所有数据
    #print alldata.query #SELECT `web_asset`.`id`, `web_asset`.`hostname`, `web_asset`.`create_date`, `web_asset`.`update_date` FROM `web_asset`

    alldata = Asset.objects.all().values('id','hostname') #指定字段
    print alldata
    print alldata.query


    ''''
    temp = Asset.objects.all()[0:2] #所有数据的0-2，分页需要
    alldata = Asset.objects.all().order_by('id') #正序
    alldata = Asset.objects.all().order_by('-id') #倒叙
    '''
    return HttpResponse('ok')