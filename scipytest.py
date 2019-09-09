# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:26:39 2019

@author: vjha1
"""

from scipy.interpolate import interp1d
import numpy as np

# =============================================================================
# x = np.linspace(0, 10, num=11, endpoint=True)
# y = np.cos(-x**2/9.0)
# f = interp1d(x, y)
# f2 = interp1d(x, y, kind='cubic')
#  
# xnew = np.linspace(0, 10, num=41, endpoint=True)
# =============================================================================
import matplotlib.pyplot as plt
# =============================================================================
# plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
# plt.legend(['data', 'linear', 'cubic'], loc='best')
# plt.show()
# 
# 
# csvxnew = np.linspace(0, 732, num=367, endpoint=True)
# a = max(csvxnew)
# print(csvxnew)
# =============================================================================

max(xcorr_array)