#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/26 14:20
# @Author  : jiayanhua
# @Site    : 
# @File    : tag.py
# @Software: PyCharm Community Edition
from django import template
#from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()


@register.simple_tag
def mymethod(v1):#自定义
    result = v1*1000
    return result

'''
@register.simple_tag
def my_input(id, arg):
    result = "<input type='text' id='%s' class='%s' />" % (id, arg,)
    return mark_safe(result)
'''