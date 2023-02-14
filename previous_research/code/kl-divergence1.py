# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 17:24:14 2022

@author: marin
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data_100Hz_walk_Dif.csv', header=None)

df1 = pd.read_csv('data_100Hz_walk_Dif.csv', header=None)
df2 = pd.read_csv('data_50Hz_walk_Dif.csv', header=None)
df3 = pd.read_csv('data_10Hz_walk_Dif.csv', header=None)

df4 = pd.read_csv('data_100Hz_walk_Dif_1126.csv', header=None)
df5 = pd.read_csv('data_100Hz_walk_Dif_1229.csv', header=None)
df6 = pd.read_csv('data_100Hz_walk_Dif_0900.csv', header=None)
df7 = pd.read_csv('data_100Hz_walk_Dif_1000.csv', header=None)
df8 = pd.read_csv('data_100Hz_walk_Dif_0756.csv', header=None)

df9 = pd.read_csv('data_50Hz_walk_Dif_1126.csv', header=None)
df10 = pd.read_csv('data_50Hz_walk_Dif_1229.csv', header=None)
df11 = pd.read_csv('data_50Hz_walk_Dif_0900.csv', header=None)
df12 = pd.read_csv('data_50Hz_walk_Dif_1000.csv', header=None)
df13 = pd.read_csv('data_50Hz_walk_Dif_0756.csv', header=None)

df14 = pd.read_csv('data_10Hz_walk_Dif_0900.csv', header=None)
df15 = pd.read_csv('data_10Hz_walk_Dif_1000.csv', header=None)
df16 = pd.read_csv('data_10Hz_walk_Dif_0756.csv', header=None)


df21 = pd.read_csv('data_100Hz_walk_Dif_16232_test.csv', header=None)
df22 = pd.read_csv('data_100Hz_walk_Dif_16356_test.csv', header=None)
df23 = pd.read_csv('data_100Hz_walk_Dif_16234_test.csv', header=None)
df24 = pd.read_csv('data_100Hz_walk_Dif_16355_test.csv', header=None)
df25 = pd.read_csv('data_100Hz_walk_Dif_16239_test.csv', header=None)

df26 = pd.read_csv('data_100Hz_walk_Dif_16236_test.csv', header=None)
df27 = pd.read_csv('data_100Hz_walk_Dif_16230_test.csv', header=None)
df28 = pd.read_csv('data_100Hz_walk_Dif_16363_test.csv', header=None)
df29 = pd.read_csv('data_100Hz_walk_Dif_16354_test.csv', header=None)
df30 = pd.read_csv('data_100Hz_walk_Dif_16231_test.csv', header=None)

df31 = pd.read_csv('data_50Hz_walk_Dif_16325_test.csv', header=None)
df32 = pd.read_csv('data_50Hz_walk_Dif_16311_test.csv', header=None)
df33 = pd.read_csv('data_50Hz_walk_Dif_16328_test.csv', header=None)
df34 = pd.read_csv('data_50Hz_walk_Dif_16305_test.csv', header=None)
df35 = pd.read_csv('data_50Hz_walk_Dif_16320_test.csv', header=None)

df36 = pd.read_csv('data_50Hz_walk_Dif_16313_test.csv', header=None)
df37 = pd.read_csv('data_50Hz_walk_Dif_16323_test.csv', header=None)
df38 = pd.read_csv('data_50Hz_walk_Dif_16324_test.csv', header=None)
df39 = pd.read_csv('data_50Hz_walk_Dif_16300_test.csv', header=None)
df40 = pd.read_csv('data_50Hz_walk_Dif_16308_test.csv', header=None)


df41 = pd.read_csv('data_10Hz_walk_Dif_1655.csv', header=None)
df42 = pd.read_csv('data_20Hz_walk_Dif_1655.csv', header=None)
df43 = pd.read_csv('data_30Hz_walk_Dif_1655.csv', header=None)
df44 = pd.read_csv('data_40Hz_walk_Dif_1655.csv', header=None)
df45 = pd.read_csv('data_50Hz_walk_Dif_1655.csv', header=None)
df46 = pd.read_csv('data_60Hz_walk_Dif_1655.csv', header=None)
df47 = pd.read_csv('data_70Hz_walk_Dif_1655.csv', header=None)
df48 = pd.read_csv('data_80Hz_walk_Dif_1655.csv', header=None)
df49 = pd.read_csv('data_90Hz_walk_Dif_1655.csv', header=None)
df50 = pd.read_csv('data_100Hz_walk_Dif_1655.csv', header=None)

df51 = pd.read_csv('data_10Hz_walk_Dif_1716.csv', header=None)
df52 = pd.read_csv('data_20Hz_walk_Dif_1716.csv', header=None)
df53 = pd.read_csv('data_30Hz_walk_Dif_1716.csv', header=None)
df54 = pd.read_csv('data_40Hz_walk_Dif_1716.csv', header=None)
df55 = pd.read_csv('data_50Hz_walk_Dif_1716.csv', header=None)
df56 = pd.read_csv('data_60Hz_walk_Dif_1716.csv', header=None)
df57 = pd.read_csv('data_70Hz_walk_Dif_1716.csv', header=None)
df58 = pd.read_csv('data_80Hz_walk_Dif_1716.csv', header=None)
df59 = pd.read_csv('data_90Hz_walk_Dif_1716.csv', header=None)
df60 = pd.read_csv('data_100Hz_walk_Dif_1716.csv', header=None)

df61 = pd.read_csv('data_100Hz_walk_Dif_kaggle_1002.csv', header=None)
df62 = pd.read_csv('data_100Hz_walk_Dif_kaggle_1024.csv', header=None)
df63 = pd.read_csv('data_100Hz_walk_Dif_kaggle_1026.csv', header=None)
df64 = pd.read_csv('data_100Hz_walk_Dif_kaggle_1034.csv', header=None)
df65 = pd.read_csv('data_100Hz_walk_Dif_kaggle_1046.csv', header=None)


def tail(df, n):
    return df.tail(n).values.tolist()

def KLD(a, b, bins=10000, epsilon=.00001):
    min_a = a.min().min()
    min_b = b.min().min()
    max_a = a.max().max()
    max_b = b.max().max()

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

'''
def KLD(a, b, bins=10000, epsilon=.00001):
    min_value=min(min(a),min(b))
    max_value=max(max(a),max(b))
    # サンプルをヒストグラムに, 共に同じ数のビンで区切る
    a_hist, _ = np.histogram(a, range=(min_value,max_value),bins=bins) 
    b_hist, _ = np.histogram(b, range=(min_value,max_value),bins=bins)
    
    # 合計を1にするために全合計で割る
    a_hist = (a_hist+epsilon)/np.sum(a_hist)
    b_hist = (b_hist+epsilon)/np.sum(b_hist)
    
    # 本来なら a の分布に0が含まれているなら0, bの分布に0が含まれているなら inf にする
    return np.sum([ai * np.log(ai / bi) for ai, bi in zip(a_hist, b_hist)])

n = KLD(df1,df2)
print(n)

def KLD(a, b, bins=10000, epsilon=.00001):
    # サンプルをヒストグラムに, 共に同じ数のビンで区切る
    a_hist, _ = np.histogram(a, bins=bins) 
    b_hist, _ = np.histogram(b, bins=bins)
    
    # 合計を1にするために全合計で割る
    a_hist = (a_hist+epsilon)/np.sum(a_hist)
    b_hist = (b_hist+epsilon)/np.sum(b_hist)
    
    # 本来なら a の分布に0が含まれているなら0, bの分布に0が含まれているなら inf にする
    return np.sum([ai * np.log(ai / bi) for ai, bi in zip(a_hist, b_hist)])



'''

hist1,age=np.histogram(df40, bins=10000)
age=age[:len(hist1)]
plt.xlabel('age',fontsize=18)
plt.ylabel('number',fontsize=18)
plt.bar(age, hist1, width=8.0)
plt.savefig('hist_50Hz_1.png')




test = df40



#print('100Hz(df1): ', KLD(test, df1))
#print('50Hz(df2): ', KLD(test, df2))
#print('10Hz(df3): ', KLD(test, df3))

#print('df4: ', KLD(test, df4))
#print('df5: ', KLD(test, df5))
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

print('----------------------------')

print('100Hz_1(df21): ', KLD(test, df21))
print('100Hz_2(df22): ', KLD(test, df22))
print('100Hz_3(df23): ', KLD(test, df23))
print('100Hz_4(df24): ', KLD(test, df24))
print('100Hz_5(df25): ', KLD(test, df25))

print('50Hz_1(df31): ', KLD(test, df31))
print('50Hz_2(df32): ', KLD(test, df32))
print('50Hz_3(df33): ', KLD(test, df33))
print('50Hz_4(df34): ', KLD(test, df34))
print('50Hz_5(df35): ', KLD(test, df35))

print('----------------------------')

print('10Hz_1(df41): ', KLD(test, df41))
print('20Hz_1(df42): ', KLD(test, df42))
print('30Hz_1(df43): ', KLD(test, df43))
print('40Hz_1(df44): ', KLD(test, df44))
print('50Hz_1(df45): ', KLD(test, df45))
print('60Hz_1(df46): ', KLD(test, df46))
print('70Hz_1(df47): ', KLD(test, df47))
print('80Hz_1(df48): ', KLD(test, df48))
print('90Hz_1(df49): ', KLD(test, df49))
print('100Hz_1(df50): ', KLD(test, df50))


kld6 = KLD(test, df6)
kld7 = KLD(test, df7)
kld8 = KLD(test, df8)
kld11 = KLD(test, df11)
kld12 = KLD(test, df12)
kld13 = KLD(test, df13)
kld14 = KLD(test, df14)
kld15 = KLD(test, df15)
kld16 = KLD(test, df16)

kld = [kld6, kld7, kld8, kld11, kld12, kld13, kld14, kld15, kld16]
#print(kld)
kld_min = min(kld)
#print(kld_min)

idx = kld.index(kld_min)
#print(idx)



if idx >= 0 and idx < 3:
    print('推定周波数は100Hzです')
if idx >= 3 and idx < 6:
    print('推定周波数は50Hzです')
if idx >= 6 and idx < 9:
    print('推定周波数は10Hzです')
    

'''
kld_str = [str(n) for n in kld]

with open('kl-divergence.csv', 'w',newline='\n') as file:
    for x in kld_str:
      file.write(x + "\n")
'''

'''
plt.figure(figsize=(10, 5))
hist, _ = np.histogram(df1,bins=10000)
plt.plot(hist, label="100Hz")
hist, _ = np.histogram(df2,bins=10000)
plt.plot(hist, label="50Hz")
hist, _ = np.histogram(df3,bins=10000)
plt.plot(hist, label="10Hz")

hist, _ = np.histogram(df4,bins=10000)
plt.plot(hist, label="100Hz2")
hist, _ = np.histogram(df5,bins=10000)
plt.plot(hist, label="100Hz3")


hist, _ = np.histogram(df6,bins=10000)
plt.plot(hist, label="100Hz1")
plt.savefig('hist_100Hz_1.png')

hist, _ = np.histogram(df7,bins=10000)
plt.plot(hist, label="100Hz2")
plt.savefig('hist_100Hz_2.png')

hist, _ = np.histogram(df8,bins=10000)
plt.plot(hist, label="100Hz3")
plt.savefig('hist_100Hz_3.png')


hist, _ = np.histogram(df9,bins=10000)
plt.plot(hist, label="50Hz3")
hist, _ = np.histogram(df10,bins=10000)
plt.plot(hist, label="50Hz4")
hist, _ = np.histogram(df11,bins=10000)
plt.plot(hist, label="50Hz5")

hist, _ = np.histogram(df12,bins=10000)
plt.plot(hist, label="10Hz2")
hist, _ = np.histogram(df13,bins=10000)
plt.plot(hist, label="10Hz3")
plt.legend(title="distribution")
plt.grid()


hist1,age=np.histogram(df6, bins=10000)
age=age[:len(hist1)]
plt.xlabel('age',fontsize=18)
plt.ylabel('number',fontsize=18)
plt.bar(age, hist1, width=8.0)
plt.savefig('hist_100Hz_1.png')

hist2,age=np.histogram(df7, bins=10000)
age=age[:len(hist2)]
plt.xlabel('age',fontsize=18)
plt.ylabel('number',fontsize=18)
plt.bar(age, hist2, width=8.0)
plt.savefig('hist_100Hz_2.png')
'''







