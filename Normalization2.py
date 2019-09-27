# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:06:00 2019

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
filename1 = 'HD_ascend.csv'
csv1 = np.genfromtxt (filename1, delimiter=",")
second = csv1[1,:]
third = csv1[2,:]

#print(csv1[:,1])
xraw1 = csv1[:,0]
yraw1 = csv1[:,1]
#yraw1 = yraw1 - 2000
plt.plot(xraw1,yraw1)


filename2 = 'HD_descend.csv'
csv2 = np.genfromtxt (filename2, delimiter=",")
second2 = csv2[1,:]
third2 = csv2[2,:]

xraw2 = csv2[:,0]
yraw2 = -1*csv2[:,1]
#yraw2 = csv2[:,1]
#yraw2 = -1*(yraw2-2000)
plt.plot(xraw2,yraw2)

plt.show()


# =============================================================================
# fig1, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
# ax1.xcorr(csv1[:,1], csv2[:,1], usevlines=True, maxlags=35, normed=True, lw=2)
# ax1.grid(True)
# 
# ax2.acorr(csv1[:,1], usevlines=True, normed=True, maxlags=35 , lw=2)
# ax2.grid(True)
# =============================================================================



f1 = interp1d(xraw1, yraw1, kind='cubic') #interpolation to 1 sample/ms
f2 = interp1d(xraw2, yraw2, kind='cubic')#csv2[:,1], kind='cubic')
#alternate interpolation method
#f1 = InterpolatedUnivariateSpline(xraw1, yraw1)
#f2 = InterpolatedUnivariateSpline(xraw2,yraw2)

ab = max(csv1[:,0])
abc = 1000 * (ab + 1)
abcd = int(abc)
csvxnew = np.linspace(0, max(csv1[:,0]), abcd, endpoint=True) #adjust x scale to accomodate

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

#normalizing
yraw3 = [0] * len(yraw1)
yraw4 = [0] * len(yraw2)
y3 = [0] * len(y1)
y4 = [0] * len(y2)
t1 = time.time()
total = t1-t0
print('Time elapsed: ', total)

for i in range(len(yraw1)):
    yraw3[i] = (yraw1[i] - min(yraw1)) / (max(yraw1) - min(yraw1))
    
print("Checkpoint2")
t1 = time.time()
total = t1-t0
print('Time elapsed: ', total)

for i in range(len(yraw2)):
    yraw4[i] = (yraw2[i] - min(yraw2)) / (max(yraw2) - min(yraw2))

print("Checkpoint3")
t1 = time.time()
total = t1-t0
print('Time elapsed: ', total)
    
for i in range(len(y1)):
    y3[i] = (y1[i] - min(y1)) / (max(y1) - min(y1)) 

print("Checkpoint4")
t1 = time.time()
total = t1-t0
print('Time elapsed: ', total)

for i in range(len(y2)):
    y4[i] = (y2[i] - min(y2)) / (max(y2) - min(y2)) 

print("Checkpoint5")
t1 = time.time()
total = t1-t0
print('Time elapsed: ', total)