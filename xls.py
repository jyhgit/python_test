#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 9:36
# @Author  : jiayanhua
# @Site    : 
# @File    : xls.py
# @Software: PyCharm Community Edition
import xlsxwriter

workbook = xlsxwriter.Workbook('xls.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A',20)
bold=workbook.add_format({'bold':True})

worksheet.write('A1','Hello word')
worksheet.write('A2','taiyan',bold)

worksheet.write(2,0,32)
worksheet.write(3,0,23.5)
worksheet.write(4,0,'=SUM(A3:A4)')

workbook.close()


