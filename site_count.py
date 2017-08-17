#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 19:19
# @Author  : jiayanhua
# @Site    : 
# @File    : site_count.py
# @Software: PyCharm Community Edition
#xlswriter
'''
1、准备
创建一个Excel文件；创建一个工作表；创建一个图标对象；定义表头，表列；准备7天数据
2、定义格式
设置整个工作表格式，边框像素加1；
定义title格式对象，边框加粗，像素1，底色#cccccc;
tiltle 居中，内容加粗
定义avg边框加粗1，数字格式小数点
3、插入数据
4、定义函数
5、设置图标宽、高、大标题，y轴小标题
'''

import xlsxwriter

workbook = xlsxwriter.Workbook('site_count.xlsx') #create excel file object
worksheet = workbook.add_worksheet() #create sheet object
chart = workbook.add_chart({'type':'column'}) #create chart object
#title
title = [u'业务名称',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日',u'平均流量']
#列
buname = [u'业务官网',u'新闻中心',u'购物频道',u'体育频道',u'亲子频道']
#数据
data = [[100,150,120,130,111,100,105],[100,150,120,130,111,100,105],[100,150,120,130,111,100,105],[100,150,120,130,111,100,105],[100,150,120,130,111,100,105]]
#定义格式
format = workbook.add_format() #create fomart object
format.set_border(1) #边框加粗 #

format_title = workbook.add_format()
format_title.set_border(1)#边框加粗，像素1
format_title.set_bg_color('#cccccc')#背景色
format_title.set_align('center') #居中
format_title.set_bold()#字体加粗

format_avg = workbook.add_format()
format_avg.set_border(1)
format_avg.set_num_format('0.00') #设置浮点位
#插入数据
worksheet.write_row('A1',title,format_title)
worksheet.write_column('A2',buname,format)
worksheet.write_row('B2',data[0],format)
worksheet.write_row('B3',data[1],format)
worksheet.write_row('B4',data[2],format)
worksheet.write_row('B5',data[3],format)
worksheet.write_row('B6',data[4],format)
#定义
def chart_series(cur_now):
    worksheet.write_formula('I'+cur_now,'=AVERAGE(B'+cur_now+':H'+cur_now+')',format_avg)
#添加一个数据系列到图标
    chart.add_series({
        'categories':'=Sheet1!$B$1:$H$1', #设置图标标签范围
        'values':'=Sheet1!$B$'+cur_now+':$H$'+cur_now, #设置图标数据范围
        'line':{'color':'black'},#设置图标线条属性
        'name':'=Sheet1!$A$'+cur_now,
    })

for row in range(2,7):
    chart_series(str(row))

#chart.set_table()
#chart.set_style(30)
chart.set_size({'width':577,'height':287})
chart.set_title({'name':u'业务流量报表'})
chart.set_y_axis({'name':'Mb/s'})

worksheet.insert_chart('A8',chart)
workbook.close()






