# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:44:25 2019

@author: vjha1
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
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
filename1 = 'HD_ascend.csv'
csv1 = np.genfromtxt (filename1, delimiter=",")
second = csv1[1,:]
third = csv1[2,:]

#print(csv1[:,1])
xraw1 = csv1[:,0]
yraw1 = csv1[:,1]
#plt.plot(xraw1,yraw1)

filename2 = 'HD_descend.csv'
csv2 = np.genfromtxt (filename2, delimiter=",")
second2 = csv2[1,:]
third2 = csv2[2,:]

xraw2 = csv2[:,0]
yraw2 = -1*csv2[:,1]
#plt.plot(xraw2,yraw2)
#plt.show()

# =============================================================================
# fig1, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
# ax1.xcorr(csv1[:,1], csv2[:,1], usevlines=True, maxlags=35, normed=True, lw=2)
# ax1.grid(True)
# 
# ax2.acorr(csv1[:,1], usevlines=True, normed=True, maxlags=35 , lw=2)
# ax2.grid(True)
# =============================================================================



f1 = interp1d(csv1[:,0], csv1[:,1], kind='cubic') #interpolation to 1 sample/ms
f2 = interp1d(csv2[:,0], yraw2, kind='cubic')#csv2[:,1], kind='cubic')
ab = max(csv1[:,0])
abc = 1000 * (ab + 1)
csvxnew = np.linspace(0, max(csv1[:,0]), num=733000, endpoint=True) #adjust x scale to accomodate

#csvxnew = np.arange(abc)

x = csv1[:,0]
y = csv1[:,1]

plt.figure(2)
plt.plot(xraw1, yraw1, 'o', csvxnew, f1(csvxnew), '--')
print("Checkpoint1")
plt.plot(xraw2, yraw2, 'o', csvxnew, f2(csvxnew), '--')
#plt.show()

y1 = f1(csvxnew)
y2 = f2(csvxnew)

#Running xcorr
plt.figure(3)
print("Checkpoint2")
lags = plt.xcorr(y1, y2, usevlines=False,  maxlags=None, normed=True, lw=2)
print("Checkpoint3")
plt.figure(6)
c = plt.xcorr(yraw1, yraw2, usevlines=True, maxlags=None, normed=False, lw=2)
#plt.show()
print("Checkpoint4")

#xcorr_array = np.correlate(y1,y2, 'full')
#peaks,_ = find_peaks(xcorr_array)
#print(peaks)

#Printing peaks found within the xcorr output
xcorr_array_raw = c[1]
xloc_xcorr_raw = c[0]
peaks1,_ = find_peaks(xcorr_array_raw)
print('Raw Peak Locations: ', peaks1)

for i in range(len(peaks1)):
    print('Peak', i, ': ', xcorr_array_raw[peaks1[i]])    
    print('Peakx', i, ': ', xloc_xcorr_raw[peaks1[i]])
    print()
    
xcorr_array = lags[1]
xloc_xcorr = lags[0]
peaks2,_ = find_peaks(xcorr_array)
print('Interpolation Peak Locations: ', peaks2)

for i in range(len(peaks2)):
    print('Interpolation Peak', i, ': ', xcorr_array[peaks2[i]])   
    print('Interpolation Peakx', i, ': ', xloc_xcorr[peaks2[i]])
    print()
    
#plt.figure(7)

#csvxnew34 = np.linspace(0, 1465999, num=1465999, endpoint=True)
#plt.plot(csvxnew34, xcorr_array)
#print('Peak 1: ', xcorr_array_raw[20])
#print('Peak 2: ', xcorr_array_raw[35])
#print('Peak 3: ', xcorr_array_raw[51])
#print('Peak 4: ', xcorr_array_raw[62])
#print('Peak 5: ', xcorr_array_raw[69])

# =============================================================================
# plt.figure(4)
# xcorr_array = np.correlate(y1,y2, 'full')
# plt.plot(xcorr_array)
# peaks, _ = find_peaks(xcorr_array)
# plt.plot(peaks, xcorr_array[peaks], "x")
# =============================================================================

#Let's try another method
# =============================================================================
# index, value = max(y1)
# index2, value2 = max(y2)
# 
# yfft1 = np.fft.fft(y1)
# yfft2 = np.fft.fft(y2)
# 
# hfft = yfft2/yfft1
# 
# magh = np.absolute(hfft)
# angh = np.angle(hfft)
# unraph = np.unwrap(angh)
# =============================================================================






#corr = signal.correlate(csv1,csv2, mode='full', method='auto')
#plt.figure(5)
#plt.plot(corr)
#HD Peaks 379387 1006257 1416870
#PJ 218165 412034 727389 1068257 1293405 1438166
t1 = time.time()
total = t1-t0
print('Time elapsed: ', total)


