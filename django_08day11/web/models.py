# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class usertype(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Gender = models.BooleanField(default=False)
    Age = models.IntegerField(default=19)
    memo = models.TextField(default='xxx')
    Createdate = models.DateTimeField(default='2017-11-19 15:32:00')
    address = models.CharField(max_length=100)
    #type = models.IntegerField(max_length=10)
    type = models.ForeignKey('usertype')
    def __str__(self):
        return self.name

#many to many
class Group(models.Model):
    Name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    group_relation =  models.ManyToManyField('Group')
    #会自动生成第三张表
    def __str__(self):
        return self.name

class Asset(models.Model): #不用关系创建时间和修改时间
    hostname = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Temp(models.Model):
    GENDER_CHOICE = {
        (u'1',u'普通用户'),
        (u'2',u'管理用户'),
        (u'3',u'超级管理员')
    }
    usertype2 = models.CharField(max_length=20,choices = GENDER_CHOICE)
