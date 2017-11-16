
# -*- coding: utf-8 -*-
# @Time    : 2017/11/8 23:30
# @Author  : jiayanhua
# @Site    : 
# @File    : wsgi.py
# @Software: PyCharm Community Edition
from wsgiref.simple_server import make_server
from View.Admin import *
from View.Account import *

'''
def login():
    #file
    #htmls
    html ='<p>username:<input /></p><p>password:<input /></p>'
    return html
def logout():
    return 'logout'
'''
urls = (
    ('/index/',index),
    ('/login/',login),
    ('/loginout/',loginout),
)
#框架如下，业务层只需要关心上面的部分
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    func = None #赋值
    for i in urls:
        if i[0] == url:
            func =  i[1]
            break #匹配到后终止循环
    if func:#判断正确
        result = func()
    else:
        return '404'
    return result
'''
    if url == '/index/':
        return "<h1>index</h1>"
    elif url ==  '/loing/':
        return "<h1>login</h1>"
    else:
        return "test"
    return '<h1>Hello, web!</h1>'
'''
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()