#!-*- coding:utf8 -*-
class TheThing(object):
	"""docstring for TheThing"""
	def __init__(self):
		self.number = 0

	def some_funcation(self):
		print "I got called."

	def add_me_up(self,more):
		self.number += more
		return self.number

a=TheThing()
b=TheThing() 	

a.some_funcation()
b.some_funcation()

print a.add_me_up(20)
print a.add_me_up(20)
print b.add_me_up(20)
print b.add_me_up(20)

print a.number
print b.number
