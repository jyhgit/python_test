#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 12:39
# @Author  : jiayanhua
# @Site    : 
# @File    : forms.py
# @Software: PyCharm Community Edition
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True,error_messages={'invaild':'格式错误'})
    #ip = forms.GenericIPAddressField()
