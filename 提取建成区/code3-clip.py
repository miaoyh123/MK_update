# coding=utf-8
# 环境设置为ArcGIS
import sys, os
import arcpy
from arcpy import *
import glob

# 2. 按掩膜提取--剪裁

input_path = r"G:\PANDA\1_copy"
shp_path = r"G:\PANDA\shp_file\hebei_province.shp"
output_path = r"G:\PANDA\2_clip_province"

# 创建文件夹
if os.path.exists(output_path)==False:
        os.mkdir(output_path)
# 定义工作空间
arcpy.env.workspace = input_path

# 得到所有tif格式影像
rasterlist_ = arcpy.ListRasters("*", "tif")
rasters = glob.glob(os.path.join(input_path, "*.tif"))

for raster in rasters:
    name_input = os.path.basename(raster).split(".")[0] + ".tif"
    name_output = os.path.join(output_path, name_input)
    print (name_output)
    arcpy.gp.ExtractByMask_sa(raster
                              , shp_path
                              , name_output)