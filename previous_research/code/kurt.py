# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 20:56:26 2022

@author: marin
"""

import pandas as pd
from scipy.stats import kurtosis

df1 = pd.read_csv('data_100Hz_walk_Dif.csv')
df2 = pd.read_csv('data_50Hz_walk_Dif.csv')
df3 = pd.read_csv('data_10Hz_walk_Dif.csv')

df4 = pd.read_csv('data_100Hz_walk_Dif_1126.csv')
df5 = pd.read_csv('data_100Hz_walk_Dif_1229.csv')
df6 = pd.read_csv('data_100Hz_walk_Dif_0900.csv')
df7 = pd.read_csv('data_100Hz_walk_Dif_1000.csv')
df8 = pd.read_csv('data_100Hz_walk_Dif_0756.csv')

df9 = pd.read_csv('data_50Hz_walk_Dif_1126.csv')
df10 = pd.read_csv('data_50Hz_walk_Dif_1229.csv')
df11 = pd.read_csv('data_50Hz_walk_Dif_0900.csv')
df12 = pd.read_csv('data_50Hz_walk_Dif_1000.csv')
df13 = pd.read_csv('data_50Hz_walk_Dif_0756.csv')

df14 = pd.read_csv('data_10Hz_walk_Dif_0900.csv')
df15 = pd.read_csv('data_10Hz_walk_Dif_1000.csv')
df16 = pd.read_csv('data_10Hz_walk_Dif_0756.csv')


#kurt = df.kurt() #尖度
print('尖度: ', kurtosis(df1))
print('尖度: ', kurtosis(df2))
print('尖度: ', kurtosis(df3))
print('尖度: ', kurtosis(df4))
print('尖度: ', kurtosis(df5))
print('尖度: ', kurtosis(df6))
print('尖度: ', kurtosis(df7))
print('尖度: ', kurtosis(df8))
print('尖度: ', kurtosis(df9))
print('尖度: ', kurtosis(df10))
print('尖度: ', kurtosis(df11))
print('尖度: ', kurtosis(df12))
print('尖度: ', kurtosis(df13))
print('尖度: ', kurtosis(df14))
print('尖度: ', kurtosis(df15))
print('尖度: ', kurtosis(df16))

#print("尖度：\n", kurt)
