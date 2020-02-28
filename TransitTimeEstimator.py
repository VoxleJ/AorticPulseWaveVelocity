# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:44:25 2019

@author: vjha1
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import math
from scipy.signal import find_peaks
import time
import sys

#===============Defining Functions=============================================
def __abs__(self):
    return (self.x ** 2 + self.y ** 2) ** 0.5

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

#===============Import and View Flows=========================================

t0 = time.time()
#Loading data
#filename1 = 'XX_ascend.csv' #Ascending flow waveform
filename1 = input('Enter the Ascending Flow Waveform Filename: ')
csv1 = np.genfromtxt (filename1, delimiter=",")
second = csv1[1,:]
third = csv1[2,:]


xraw1 = csv1[:,0]
yraw1 = csv1[:,1]
plt.plot(xraw1,yraw1, 'o')


#filename2 = 'XX_descend.csv' #Descending flow waveform
filename2 = input('Enter the Descending Flow Waveform Filename: ')
csv2 = np.genfromtxt (filename2, delimiter=",")
second2 = csv2[1,:]
third2 = csv2[2,:]

xraw2 = csv2[:,0]
yraw2 = -1*csv2[:,1]
plt.plot(xraw2,yraw2, 'o')


ab = max(csv1[:,0])
abc = 1000 * (ab + 1)
abcd = int(abc)
#adjust x scale to accomodate interpolated values
csvxnew = np.linspace(0, max(csv1[:,0]), abcd, endpoint=True) 

x = csv1[:,0]
y = csv1[:,1]
yraw3 = [0] * len(yraw1)
yraw4 = [0] * len(yraw2)

#================Normalizing===================================================
for i in range(len(yraw1)):
    yraw3[i] = (yraw1[i] - min(yraw1)) / (max(yraw1) - min(yraw1))
    
#print("Checkpoint1")
#t1 = time.time()
#total = t1-t0
#print('Time elapsed: ', total, 's')

for i in range(len(yraw2)):
    yraw4[i] = (yraw2[i] - min(yraw2)) / (max(yraw2) - min(yraw2))

#print("Checkpoint2")
#t1 = time.time()
#total = t1-t0
#print('Time elapsed: ', total, 's')

f1 = interp1d(xraw1, yraw3, kind='cubic') #interpolation to 1 sample/ms
f2 = interp1d(xraw2, yraw4, kind='cubic')#csv2[:,1], kind='cubic')

#print("Checkpoint3")
#t1 = time.time()
#total = t1-t0
#print('Time elapsed: ', total, 's')

y1 = f1(csvxnew)
y2 = f2(csvxnew)

plt.figure(2)
#plt.plot(xraw1, yraw3, 'o', csvxnew, f1(csvxnew), '--')
plt.plot(csvxnew, y1, '--')
plt.plot(csvxnew, y2, '--')
#print("Checkpoint4")

#plt.plot(xraw2, yraw4, 'o', csvxnew, f2(csvxnew), '--')

#plt.show()

my1 = max(y1)
my2 = max(y2)

TT_method = input("Please choose a TT Point method 20, 25 or 50: ")

TT_method = int(float(TT_method))

if TT_method == 20:
    print("20% Selected")
    half1 = 0.20*my1
    half2 = 0.20*my2

elif TT_method == 25:
    print("25% Selected")
    half1 = 0.25*my1
    half2 = 0.25*my2

elif TT_method == 50:
    print("50% Selected")
    half1 = 0.50*my1
    half2 = 0.50*my2 

else:
    print("Invalid Value")   
    
ii = 1

#================Finding peak location for each flow===========================
nmax1 = find_nearest(y1, my1)
nmax2 = find_nearest(y2, my2) 
nmax1loc = np.where(y1 == nmax1)
nmax2loc = np.where(y2 == nmax2)

nmax1loc = nmax1loc[0]
a1 = list(nmax1loc)
nmax1loc = int(a1[0])

nmax2loc = nmax2loc[0]
a2 = list(nmax2loc)
nmax2loc = int(a2[0])

y3 = y1[0:nmax1loc]
y4 = y2[0:nmax2loc] #sets new boundary at peak to avoid incorrect values

nhalf1 = find_nearest(y3, half1)
nhalf2 = find_nearest(y4, half2)

my1loc = np.where(y1 == nhalf1)#y1.index(half1)
my2loc = np.where(y2 == nhalf2) #y2.index(half2)


TA = csvxnew[my1loc]
TD = csvxnew[my2loc]

TT2 = TD - TA
TT = TA - TD

TA = csvxnew[my1loc]
TD = csvxnew[my2loc]
#print('TA: ', TA)
#print('TD: ', TD)
TT = TA - TD
TT2 = TD - TA
#distance = math.sqrt( ((TA-TD)**2)+((nhalf1-nhalf2)**2) )

#print('TT TA-TD: ', TT, ' ms')
#print()
print('TT: ', TT2, ' ms')
print()

answer = input('Do you want to continue? (y/n): ')
if answer.lower().startswith("y"):
      print()
      print("XCorr Method")
elif answer.lower().startswith("n"):
      print("Exit Script")
      sys.exit()
      
#t1 = time.time()
#total = t1-t0
#print('Time elapsed: ', total, 's')   

#Running xcorr
plt.figure(5)
#print("Checkpoint5")
lags = plt.xcorr(y1, y2, usevlines=False,  maxlags=None, normed=True, lw=2)
t1 = time.time()
total = t1-t0
#print('Time elapsed: ', total, 's')

#print("Checkpoint6")
plt.figure(6)
c = plt.xcorr(yraw3, yraw4, usevlines=True, maxlags=None, normed=True, lw=2)
t1 = time.time()
total = t1-t0
#print('Time elapsed: ', total, 's')

#plt.show()
#print("Checkpoint7")

#xcorr_array = np.correlate(y1,y2, 'full')
#peaks,_ = find_peaks(xcorr_array)
#print(peaks)

#Printing peaks found within the xcorr output
xcorr_array_raw = c[1]
xloc_xcorr_raw = c[0]
peaks1,_ = find_peaks(xcorr_array_raw)
#print('Raw Peak Locations: ', peaks1)

#for i in range(len(peaks1)):
#    print('Peak', i, ': ', xcorr_array_raw[peaks1[i]])    
#    print('Peakx', i, ': ', xloc_xcorr_raw[peaks1[i]])
#    print()
    
xcorr_array = lags[1]
xloc_xcorr = lags[0]
peaks2,_ = find_peaks(xcorr_array)
peaky = [0]*20
peakx = [0]*20
#print('Interpolation Peak Locations: ', peaks2)
#=========Choose the peak with the highest correlation (peaky = 1)============#
ij = 0

for i in range(len(peaks2)):
#    print('Interpolation Peaky', i, ': ', xcorr_array[peaks2[i]])   
#    print('Interpolation Peakx', i, ': ', xloc_xcorr[peaks2[i]])
    peaky[ij] = xcorr_array[peaks2[i]]
    peakx[ij] = xloc_xcorr[peaks2[i]]
#    print()
    ij = ij + 1
    
max_ind = np.argwhere(peaky == find_nearest(peaky, 0.99))
xtransittime = peakx[max_ind[0,0]]
xtransittime = abs(xtransittime) * 1e-6
xtransr = round(xtransittime, 4)

#==========================Output final results===============================#
print(filename1)
print('XCorr Transit Time: ', xtransr, 's')

t1 = time.time()
total = (t1-t0)/60
rtotal = round(total, 2)
print('Total Time elapsed: ', rtotal, 'min')
plt.show()
