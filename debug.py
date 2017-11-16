#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
def show():
	print('a')
	if 1 == 1:
		return [11,22]
	print('b')

ret=show()

def show_1(arg):
	print(arg)
n=[11,22,33,44]
show_1(n)

def show(*arg):#转换成元组
	print(arg,type(arg))
show(1)
show(11,22,33)

def show(**args):#转成字典
	print(args,type(args))
show(n1=123,uu=234,bb=000)


def show(*args,**kwargs):#顺序不能变，两个星在后
	print(args,type(args))
	print(kwargs,type(kwargs))
ll=[11,22,33]
dir={'n1':88,'alex':'dfs'}
show(*ll,**dir)
#show(11,22,33,n1=88,alex='dfds')#同上，

#动态参数应用
s1="{0} is {1}"  #占位
#result=s1.format('alex','sx')
#print(result)
L=['alex','sb']
result=s1.format(*L)

print(result)

s2='{name} is {acter}'
dir={'name':'alex','acter':'sx'}
result2=s2.format(**dir)
print(result2)
"""
# def func(a):
# 	b = a + 1
# 	# return
# 	# return b
# 	# return b
# func(99)
# xxx





