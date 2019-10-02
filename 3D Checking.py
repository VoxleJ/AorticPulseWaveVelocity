# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:06:52 2019

@author: vjha1
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

filename1 = 'MD_distance.csv'
csv1 = np.genfromtxt (filename1, delimiter=",")

fig = plt.figure()
ax = fig.gca(projection='3d')

xraw1 = csv1[:,0]
yraw1 = csv1[:,1]
zraw1 = csv1[:,2]

plt.plot(xraw1, yraw1, zraw1 ,  lw = 10)
plt.show()
