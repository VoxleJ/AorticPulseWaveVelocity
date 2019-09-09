# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:56:40 2019

@author: vjha1
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import time

t0 = time.time()
filename1 = 'LS_ascend.csv'
csv1 = np.genfromtxt (filename1, delimiter=",")
second = csv1[1,:]
third = csv1[2,:]

#print(csv1[:,1])
xraw1 = csv1[:,0]
yraw1 = csv1[:,1]
plt.plot(xraw1,yraw1)

filename2 = 'LS_descend.csv'
csv2 = np.genfromtxt (filename2, delimiter=",")
second2 = csv2[1,:]
third2 = csv2[2,:]

xraw2 = csv2[:,0]
yraw2 = -1* csv2[:,1]
plt.plot(xraw2,yraw2)


# =============================================================================
# fig1, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
# ax1.xcorr(csv1[:,1], csv2[:,1], usevlines=True, maxlags=35, normed=True, lw=2)
# ax1.grid(True)
# 
# ax2.acorr(csv1[:,1], usevlines=True, normed=True, maxlags=35 , lw=2)
# ax2.grid(True)
# =============================================================================



f1 = interp1d(csv1[:,0], csv1[:,1], kind='cubic') #interpolation to 1 sample/ms
f2 = interp1d(csv2[:,0], csv2[:,1], kind='cubic')

ab = max(csv1[:,0])
#print (ab)
abc = 1000 * (ab + 1)
#print(abc)
xc = np.arange(abc)
t1 = time.time()

total = t1-t0
print('Elapsed time: ', total)
#csvxnew = np.linspace(0,    ab), num=abc, endpoint=True) #adjust x scale to accomodate
