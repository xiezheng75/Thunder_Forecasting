import os
import requests
import pandas as pd
import numpy as np
from io import StringIO
from osgeo import gdal
import matplotlib.pyplot as plt


# 打开.img文件
dataset = gdal.Open('G:/Other computers/My PC/PolyU_PhD/Thesis/Data/B50K_R200index-geo.tif')
# 检查文件是否成功打开
if dataset is None:
    print('文件打开失败')
else:
    # 读取第一波段的数据
    band = dataset.GetRasterBand(1)
    data = band.ReadAsArray()
# data是一个numpy数组，包含了该波段的栅格数据
    print(data)

 # Check and print unique values in the data
    unique_values = np.unique(data)
    print(f'Unique values: {unique_values}')
# Check total number of unique values
    num_unique_values = len(unique_values)
    print(f'Number of unique values: {num_unique_values}')

# 获取数据的最大值和最小值
    print(f'最大值：{np.max(data)}')
    print(f'最小值：{np.min(data)}')
# 获取数据的数据类型

    print(f'数据类型：{data.dtype}')
# 获取数据的NoData值
    no_data_value = band.GetNoDataValue()
    print(f'NoData值：{no_data_value}')
# 获取数据的统计信息
    stats = band.GetStatistics(True, True)
    print(f'统计信息：{stats}')
# 获取数据的直方图
    hist = band.GetHistogram(stats[0], stats[1], int(stats[2]), include_out_of_range=False, approx_ok=False)
    print(f'直方图：{hist}')
# 获取数据的坐标系
#    projection = dataset.GetProjection()
#    print(f'坐标系：{projection}')

# 获取影像的尺寸
    rows, cols = dataset.RasterYSize, dataset.RasterXSize
    print(f'影像尺寸：{rows} x {cols}')
# 获取影像的地理变换信息，例如仿射变换参数
    geo_transform = dataset.GetGeoTransform()
    print(f'地理变换信息：{geo_transform}')
# 获取影像的投影信息
    projection = dataset.GetProjection()
    print(f'投影信息：{projection}')
# 关闭数据集
    dataset = None


# ds = gdal.Open('G:/Other computers/My PC/PolyU_PhD/Thesis/Data/MOD12Q2.A2003193.h28v06.004.hdf')
# band = ds.GetRasterBand(1)  # 读取第一个波段
# data = band.ReadAsArray()
# print(data)
# plt.imshow(data)
# plt.colorbar()
# plt.show()