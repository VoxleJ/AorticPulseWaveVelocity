# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:31:20 2019

@author: vjha1
"""

#TT 50

#import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import interp1d
#from scipy import signal
#from scipy.signal import find_peaks
import time
#import operator
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

t0 = time.time()
#Loading data
filename1 = 'JH_ascend.csv'
csv1 = np.genfromtxt (filename1, delimiter=",")
second = csv1[1,:]
third = csv1[2,:]

#print(csv1[:,1])
xraw1 = csv1[:,0]
yraw1 = csv1[:,1]
#plt.plot(xraw1,yraw1)

filename2 = 'JH_descend.csv'
csv2 = np.genfromtxt (filename2, delimiter=",")
second2 = csv2[1,:]
third2 = csv2[2,:]

xraw2 = csv2[:,0]
yraw2 = -1*csv2[:,1]

#f1 = interp1d(csv1[:,0], csv1[:,1], kind='cubic') #interpolation to 1 sample/ms
#f2 = interp1d(csv2[:,0], yraw2, kind='cubic')#csv2[:,1], kind='cubic')
ab = max(csv1[:,0])
abc = 1000 * (ab + 1)
csvxnew = np.linspace(0, max(csv1[:,0]), num=733000, endpoint=True)

#y1 = f1(csvxnew)
#y2 = f2(csvxnew)

my1 = max(yraw1)
my2 = max(yraw2)

half1 = 0.50*my1
half2 = 0.50*my2

nhalf1 = find_nearest(yraw1, half1)
nhalf2 = find_nearest(yraw2, half2)

my1loc = np.where(yraw1 == nhalf1)#y1.index(half1)
my2loc = np.where(yraw2 == nhalf2) #y2.index(half2)



TA = xraw1[my1loc] #csvxnew[]
TD = xraw2[my2loc]
print(TA)
print(TD)
TT = TA - TD
TT2 = TD - TA
distance = math.sqrt( ((TA-TD)**2)+((nhalf1-nhalf2)**2) )

print('TT TA-TD: ', TT)
print()
print('TT TD-TA: ', TT2)
print()
print('Distance: ', distance)

t1 = time.time()
total = t1-t0
#print('Time elapsed: ', total)