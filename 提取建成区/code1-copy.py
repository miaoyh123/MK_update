# coding=utf-8
# 环境设置为ArcGIS
import sys, os
import arcpy
from arcpy import *
import glob

# 1. 栅格识别与复制
input_path = r"G:\global NTL\PANDA"
output_path = r"G:\global NTL\PANDA\1_copy"

# 创建文件夹
if os.path.exists(output_path)==False:
        os.mkdir(output_path)

# 批量复制
for root, dirs, files in os.walk(input_path):
    for each_file in files:
        if each_file.startswith('PANDA') and each_file.endswith('.tif'):
            path = os.path.join(root,each_file)
            copy_path = output_path + '\\' + each_file
            print (copy_path)
            arcpy.CopyRaster_management(path, copy_path, "", "", format="TIFF")