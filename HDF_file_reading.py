import os
import requests
import pandas as pd
import numpy as np
from io import StringIO
from osgeo import gdal
import matplotlib.pyplot as plt
import h5py
# from pyhdf.SD import SD


# 打开HDF文件
hdf_file = 'G:/Other computers/My PC/PolyU_PhD/Thesis/Data/MOD12Q1.A2004001.h28v06.004.hdf'
dataset = gdal.Open(hdf_file)

# 获取子数据集列表
subdatasets = dataset.GetSubDatasets()
print(subdatasets)
# 遍历子数据集
for i, subdataset in enumerate(subdatasets):
    # 获取子数据集的名称和描述
    subdataset_name = subdataset[0]
    subdataset_desc = subdataset[1]

    print(f'Subdataset {i + 1}:')
    print(f'  Name: {subdataset_name}')
    print(f'  Description: {subdataset_desc}\n')

    # 打开子数据集
    subdataset_ds = gdal.Open(subdataset_name)

    # 读取波段数据
    if subdataset_ds:
        band = subdataset_ds.GetRasterBand(1)  # 假设我们读取第一个波段
        data = band.ReadAsArray()

        # 打印数据数组的形状（大小）
        print(f'  Data shape: {data.shape}')
        # 打印数组数据
        print(f'  Data:\n{data}\n')

# # 打开HDF文件
# file_path = 'G:/Other computers/My PC/PolyU_PhD/Thesis/Data/MOD12Q2.A2003193.h28v06.004.hdf'
# with SD.File(file_path, 'r') as file:
#     # 打印文件中的数据集名称
#     print(list(file.keys()))
#
#     # # 假设我们要读取的数据集名称为'dataset_name'
#     # dataset = file['dataset_name']
#     #
#     # # 读取数据
#     # data = dataset[:]
#     # print(data)