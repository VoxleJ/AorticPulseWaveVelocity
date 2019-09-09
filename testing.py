# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:46:33 2019

@author: vjha1
"""
print("hello")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv


# Fixing random state for reproducibility
np.random.seed(19680801)

csv_file = r"output.csv"

x, y = np.random.randn(2, 100)
fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax1.grid(True)

ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax2.grid(True)

plt.show()

filename = 'series12001-Body_Flow_L1_output.txt'
file = open(filename, mode = 'rt')
text = file.read()
values = file.readlines()
file.close()

#intxt = csv.reader(open(filename, 'rb'),delimiter = '\t')
#outcsv = csv.writer(open(csv_file, 'wb'))
#outcsv.writerows(intxt)
#print(text)

#df = pd.read_fwf(filename)
#df.to_csv('output.csv')
#doesn't work with output.txt files

print(text)


with open(filename, 'rt') as myfile:
    for myline in myfile:
        print(myline)

myfile.close()

mylines = []
with open(filename, 'rt') as myfile:
    for line in myfile:
        mylines.append(line)
    for element in mylines:
        print(element, end=' ')

ab = mylines[29:59]

dlist = ''.join(ab)
darray = []
for item in dlist.split(';'):
    darray.append(item)

b = []