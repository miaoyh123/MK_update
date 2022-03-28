# 环境设置为conda
# 导入模块
import numpy as np
import pandas as pd
import os
from dbfread import DBF
import xlwt
# 读取dbf所在文件路径，shp
files=r"G:\PANDA\2_clip_province"
dbf_filename=[]
for i in os.listdir(files):
    if i.endswith('.dbf'):
        file_path = os.path.join(files,i)
        dbf_filename.append(file_path)
dbf_filename

# 将dbf文件批量转为xls文件
for each_dbf in dbf_filename:
    xls_filename = each_dbf.replace('dbf','xls')
    # 数据表文件名
    table = DBF(each_dbf, encoding='utf-8')
    all_sheet = []
    book = xlwt.Workbook()                  # 新建一个excel
    sheet = book.add_sheet('all_sheet')     # 添加一个sheet页
    row = 0     # 控制行数
    write_row = 0
    sheet_list = []
    for record in table:
        col = 0
        if all_sheet == []:                 # 这个为了控制只读取字段名一次
            sheet_dict = record.keys()
            # print(type(sheet_dict))         # <class 'odict_keys'>
            # sheet_list = list(set(sheet_dict))  # 将odict_keys转化为列表进行操作,这样xls的表头(第一行)会和原来的dbf顺序不一致
            sheet_list = list(sheet_dict)  # 将odict_keys转化为列表进行操作,这样操作顺序和原来的一样
            all_sheet = sheet_list
        if write_row == 0:                  # 为了控制只将字段名写入一次
            col = 0
            for i in range(len(sheet_list)):
                sheet.write(row, col, sheet_list[i])
                col += 1
            col = 0
            row += 1
            write_row += 1
        for field in record:
            sheet.write(row, col, record[field])
            # print(field,'=',record[field],end='')
            col += 1
        row += 1
    file_path = os.path.join(files,xls_filename)
    book.save(file_path)
