# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from web.models import Asset
from django.shortcuts import render_to_response
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
    obj = Asset.objects.get(id=id) #get只能获取一条数据，只要获取不到就报错
    obj.hostname = hostname
    obj.save()
    '''
    Asset.objects.filter(id__gt=id),update(hostname=hostname) #批量修改大于指定id的hostnme全部修改
    return HttpResponse('ok')

def Get(request,hostname):
    assetlist = Asset.objects.filter(hostname__contains=hostname) #fileter 获取多条数据，没有数据不会报错。而且与get获取的类型不一样，get获取到一个对象，filter获取多个对象的集合
    #for item in assetlist:#循环列出id
    #    print item.id
    #print assetlist

    #alldata = Asset.objects.all() #所有数据
    #print alldata.query #SELECT `web_asset`.`id`, `web_asset`.`hostname`, `web_asset`.`create_date`, `web_asset`.`update_date` FROM `web_asset`

    alldata = Asset.objects.all().values('id','hostname') #映射字段，返回指定字段
    print alldata
    print alldata.query


    ''''
    temp = Asset.objects.all()[0:2] #所有数据的0-2，分页需要
    alldata = Asset.objects.all().order_by('id') #正序
    alldata = Asset.objects.all().order_by('-id') #倒叙
    '''
    return HttpResponse('ok')

def AssetList(request):
    assetlist = Asset.objects.all()
    result = render_to_response('assetlist.html',{'data':assetlist,'user':"jiayanhua"}) #将数据嵌入到html
    return result