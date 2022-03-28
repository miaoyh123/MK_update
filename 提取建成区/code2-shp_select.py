# coding=utf-8
# 环境设置为ArcGIS
import arcpy
from arcpy import env
from arcpy.sa import *

input_path = r"E:\ArcGIS data\2019全国行政区划\市.shp" # 全国shp文件路径
output_path = r"G:\PANDA\shp_file\hebei_province.shp"

# 创建文件夹
if os.path.exists(output_path)==False:
        os.mkdir(output_path)

# 设置环境
env.workspace = r"E:\ArcGIS data\2019全国行政区划"

# 设置SQL提取语句
inSQLClause = """ "省代码" = 130000 """ # 河北省的省份代码为130000，前面的"省代码"是shp图层的字段名称~

# 按属性提取shp文件
arcpy.Select_analysis(input_path, output_path, inSQLClause)