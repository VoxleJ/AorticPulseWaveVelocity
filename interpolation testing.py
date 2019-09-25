# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:56:40 2019

@author: vjha1
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.signal import find_peaks
import time

t0 = time.time()
filename1 = 'GS_pre_ascend.csv'
csv1 = np.genfromtxt (filename1, delimiter=",")
second = csv1[1,:]
third = csv1[2,:]

#print(csv1[:,1])
xraw1 = csv1[:,0]
yraw1 = csv1[:,1]
yraw1 = yraw1 - 2100 #This adjustment is for some specific data
plt.plot(xraw1,yraw1, 'o')

filename2 = 'GS_pre_descend.csv'
csv2 = np.genfromtxt (filename2, delimiter=",")
second2 = csv2[1,:]
third2 = csv2[2,:]

xraw2 = csv2[:,0]
yraw2 = -1* csv2[:,1]
yraw2 = -1 * (yraw2 - 2000) #This adjustment is for some specific data
plt.plot(xraw2,yraw2,'o')


# =============================================================================
# fig1, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
# ax1.xcorr(csv1[:,1], csv2[:,1], usevlines=True, maxlags=35, normed=True, lw=2)
# ax1.grid(True)
# 
# ax2.acorr(csv1[:,1], usevlines=True, normed=True, maxlags=35 , lw=2)
# ax2.grid(True)
# =============================================================================



f1 = interp1d(xraw1, yraw1, kind='cubic') #interpolation to 1 sample/ms
f2 = interp1d(xraw2, yraw2, kind='cubic')

ab = max(csv1[:,0])
abc = 1000 * (ab + 1)
abcd = int(abc)
csvxnew = np.linspace(0, max(csv1[:,0]), abcd, endpoint=True)

plt.figure(4)
lags = plt.xcorr(y1, y2, usevlines=False,  maxlags=None, normed=True, lw=2)
xcorr_array = lags[1]
xloc_xcorr = lags[0]
peaks2,_ = find_peaks(xcorr_array)
print('Interpolation Peak Locations: ', peaks2)

for i in range(len(peaks2)):
    print('Interpolation Peak', i, ': ', xcorr_array[peaks2[i]])   
    print('Interpolation Peakx', i, ': ', xloc_xcorr[peaks2[i]])
    print()
    
print(filename1)

t1 = time.time()

total = t1-t0
print('Elapsed time: ', total)
#csvxnew = np.linspace(0,    ab), num=abc, endpoint=True) #adjust x scale to accomodate
