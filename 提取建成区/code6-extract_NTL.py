# coding=utf-8
# 环境设置为ArcGIS

import sys, os
import arcpy
from arcpy import *
import glob

input_path = r"G:\PANDA\2_clip_province" # 输入栅格数据的文件夹路径
output_path = r"G:\PANDA\4_extract" # 输出栅格所在的文件夹路径

# 创建文件夹
if os.path.exists(output_path)==False:
        os.mkdir(output_path)

# 定义工作空间
arcpy.env.workspace = input_path

# 得到所有tif格式影像
rasterlist = arcpy.ListRasters("*", "tif")
rasters = glob.glob(os.path.join(input_path, "*.tif"))

# 获取每年要提取的值
list_df = [25, 22, 19, 20, 20] # 要根据MK代码写入每年的提取值

dicts = dict(zip(rasters,list_df))

for raster in rasters:
    name_input = os.path.basename(raster).split(".")[0] + ".tif"
    name_output = os.path.join(output_path, name_input)
    print (name_output)
    arcpy.gp.ExtractByAttributes_sa(raster, """"VALUE" >=%s"""%(dicts[raster]),name_output) # 按属性提取