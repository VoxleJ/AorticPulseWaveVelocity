# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:03:24 2019

@author: vjha1
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import InterpolatedUnivariateSpline
#from scipy import signal
from scipy.signal import find_peaks
import time
#import operator

def __abs__(self):
    return (self.x ** 2 + self.y ** 2) ** 0.5

# =============================================================================
# filename1 = 'PJ_ascend.csv'
# file = open(filename1, mode = 'rt')
# text = file.read()
# values = file.readlines()
# file.close()
# 
# =============================================================================
# =============================================================================
# print(text)
# print('aa,bc')
# print(values)
# 
# reader = csv.reader(filename.split('\n'), delimiter=',')
# for row in reader:
#     print('\t'.join(row))
# 
# f = StringIO(filename)
# reader = csv.reader(f, delimiter=',')
# for row in reader:
#     print('\t'.join(row))
#    
# d = values(1)
# =============================================================================
t0 = time.time()
#Loading data
filename1 = 'LS_ascend.csv'
csv1 = np.genfromtxt (filename1, delimiter=",")
second = csv1[1,:]
third = csv1[2,:]

#print(csv1[:,1])
xraw1 = csv1[:,0]
yraw1 = csv1[:,1]
#yraw1 = yraw1 - 2000
plt.plot(xraw1,yraw1)


filename2 = 'LS_descend.csv'
csv2 = np.genfromtxt (filename2, delimiter=",")
second2 = csv2[1,:]
third2 = csv2[2,:]

xraw2 = csv2[:,0]
yraw2 = -1*csv2[:,1]
#yraw2 = csv2[:,1]
#yraw2 = -1*(yraw2-2000)
plt.plot(xraw2,yraw2)
plt.show()

print(len(yraw1))
plt.figure(2)
yraw3 = [0]*len(yraw1)
yraw4 = [0]*len(yraw2)

for i in range(len(yraw1)):
    yraw3[i] = (yraw1[i] - min(yraw1)) / (max(yraw1) - min(yraw1))


for i in range(36):
    yraw4[i] = (yraw2[i] - min(yraw2)) / (max(yraw2) - min(yraw2))
    
plt.plot(xraw1, yraw3)
plt.plot(xraw2,yraw4)

plt.show()
