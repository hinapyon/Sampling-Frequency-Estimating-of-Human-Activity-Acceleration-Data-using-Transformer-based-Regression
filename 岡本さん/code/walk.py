# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:31:06 2022

@author: marin
"""

import csv
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import pandas as pd

accX = []
accY = []
accZ = []

df6 = pd.read_csv('data_100Hz_walk_Dif_0900.csv', header=None)
df7 = pd.read_csv('data_100Hz_walk_Dif_1000.csv', header=None)
df8 = pd.read_csv('data_100Hz_walk_Dif_0756.csv', header=None)

df11 = pd.read_csv('data_50Hz_walk_Dif_0900.csv', header=None)
df12 = pd.read_csv('data_50Hz_walk_Dif_1000.csv', header=None)
df13 = pd.read_csv('data_50Hz_walk_Dif_0756.csv', header=None)

df14 = pd.read_csv('data_10Hz_walk_Dif_0900.csv', header=None)
df15 = pd.read_csv('data_10Hz_walk_Dif_1000.csv', header=None)
df16 = pd.read_csv('data_10Hz_walk_Dif_0756.csv', header=None)

df17 = pd.read_csv('data_50Hz_walk_Dif_16311.csv', header=None)

df21 = pd.read_csv('data_100Hz_walk_Dif_16232.csv', header=None)
df22 = pd.read_csv('data_100Hz_walk_Dif_16356.csv', header=None)
df23 = pd.read_csv('data_100Hz_walk_Dif_16234.csv', header=None)
df24 = pd.read_csv('data_100Hz_walk_Dif_16355.csv', header=None)
df25 = pd.read_csv('data_100Hz_walk_Dif_16239.csv', header=None)


df26 = pd.read_csv('data_50Hz_walk_Dif_16325.csv', header=None)
df27 = pd.read_csv('data_50Hz_walk_Dif_16311.csv', header=None)
df28 = pd.read_csv('data_50Hz_walk_Dif_16328.csv', header=None)
df29 = pd.read_csv('data_50Hz_walk_Dif_16305.csv', header=None)
df30 = pd.read_csv('data_50Hz_walk_Dif_16320.csv', header=None)


number = 1046
Hz = 100
#filename = '{0}Hz.csv'.format(number)
#filename = 'walk{0}Hz-0809-0900.csv'.format(Hz)
#filename = '50Hz/HASC{0}-acc.csv'.format(number)
#filename = 'HASC15000-acc.csv'
filename = 'kaggle/{0}.csv'.format(number)
#filename = 'data/mem-{0}Hz-20230117-1655.csv'.format(Hz)
#filename = 'data/mem-{0}Hz-20230117-1716.csv'.format(Hz)

with open(filename) as f: #ｘ軸,y軸,z軸の値を配列に格納
    reader = csv.reader(f)
    for row in reader:
        accX.append(float(row[1]))
        accY.append(float(row[2]))
        accZ.append(float(row[3]))

#3軸それぞれの加速度の平均を計算
sumX:float = 0
sumY:float = 0
sumZ:float = 0
index = 0

for add in accX:
    sumX = sumX + accX[index]
    index += 1

index = 0
for add in accY:
    sumY = sumY + accY[index]
    index += 1

index = 0
for add in accZ:
    sumZ = sumZ + accZ[index]
    index += 1

aveX = sumX / index
aveY = sumY / index
aveZ = sumZ / index

#加速度の平均の合成値
aveAcc = math.sqrt(aveX * aveX + aveY * aveY + aveZ * aveZ)
print(aveAcc)

#それぞれの加速度の合成値
index = 0
acc = []
for walk in zip(accX, accY, accZ):
    com = math.sqrt(accX[index] * accX[index] + accY[index] * accY[index] + accZ[index] * accZ[index])
    acc.append(com)
    index += 1

acc_str = [str(n) for n in acc]

with open('data_{0}Hz.csv'.format(Hz), 'w',newline='\n') as file:
    for x in acc_str:
      file.write(x + "\n")

#それぞれの加速度の合成値が加速度の平均の合成値の0.9倍から1.1倍が続くと静止とする
index = 0
n = 0
for stop in acc:
    if stop < aveAcc * 1.1 and stop > aveAcc * 0.9:
        index += 1
        if index == 5:
            del acc[n-5:n]
            index = 0
    else:
        index = 0
    n += 1

acc_str = [str(n) for n in acc]

with open('data_{0}Hz_walk.csv'.format(Hz), 'w',newline='\n') as file:
    for x in acc_str:
      file.write(x + "\n")

#差分をとる
index = 0
accDif = []
for dif in acc[:-1]:
    accDif.append(math.fabs(acc[index + 1]*100000 - acc[index]*100000))
    index += 1

#リストを昇順にソート
accDif.sort()

##リストを降順にソート
#accDif.sort(reverse=True)

accDif_str = [str(n) for n in accDif]

with open('data_100Hz_walk_Dif_kaggle_{0}.csv'.format(number), 'w',newline='\n') as file:
    for x in accDif_str:
      file.write(x + "\n")


def KLD(a, b, bins=10000, epsilon=.00001):
    min_a = min(a)
    min_b = min(b)
    max_a = max(a)
    max_b = max(b)

    min_value=min(min_a,min_b)
    max_value=max(max_a,max_b)
    # サンプルをヒストグラムに, 共に同じ数のビンで区切る
    a_hist, _ = np.histogram(a, range = (min_value, max_value), bins=bins)
    b_hist, _ = np.histogram(b, range = (min_value, max_value), bins=bins)

    # 合計を1にするために全合計で割る
    a_hist = (a_hist+epsilon)/np.sum(a_hist)
    b_hist = (b_hist+epsilon)/np.sum(b_hist)

    # 本来なら a の分布に0が含まれているなら0, bの分布に0が含まれているなら inf にする
    return np.sum([ai * np.log(ai / bi) for ai, bi in zip(a_hist, b_hist)])

test = accDif


print('100Hz_1(df6): ', KLD(test, df6))
print('100Hz_2(df7): ', KLD(test, df7))
print('100Hz_3(df8): ', KLD(test, df8))

#print('df9: ', KLD(test, df9))
#print('df10: ', KLD(test, df10))
print('50Hz_1(df11): ', KLD(test, df11))
print('50Hz_2(df12): ', KLD(test, df12))
print('50Hz_3(df13): ', KLD(test, df13))

print('10Hz_1(df14): ', KLD(test, df14))
print('10Hz_2(df15): ', KLD(test, df15))
print('10Hz_3(df16): ', KLD(test, df16))

print('50Hz_4(df17): ', KLD(test, df17))

print('100Hz_1(df21): ', KLD(test, df21))
print('100Hz_2(df22): ', KLD(test, df22))
print('100Hz_3(df23): ', KLD(test, df23))
print('100Hz_4(df24): ', KLD(test, df24))
print('100Hz_5(df25): ', KLD(test, df25))

print('50Hz_1(df26): ', KLD(test, df26))
print('50Hz_2(df27): ', KLD(test, df27))
print('50Hz_3(df28): ', KLD(test, df28))
print('50Hz_4(df29): ', KLD(test, df29))
print('50Hz_5(df30): ', KLD(test, df30))
'''

print(acc[0:11].replace(',','\n'))
print(len(acc))

with open('data.csv', 'w') as file:
    for x in acc:
      file.write(x+"\r\n")

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(s_n)

print(subX)
print(subY)
print(subZ)
print(index)
print(aveX)
print(aveY)
print(aveZ)

print(aveX * aveX)
print(aveY * aveY)
print(aveZ * aveZ)
print(aveX * aveX + aveY * aveY + aveZ * aveZ)
print(aveAcc)

sumX = 0
squX = 0
subX = 0
index = 0

for var in accX:
    subX = accX[index] - aveX
    squX = subX * subX
    sumX = sumX + squX
    index += 1
    print(sumX)


varX = sumX / index
print(varX)
'''
