import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
#from scipy.interpolate import InterpolatedUnivariateSpline
import math
#from scipy import signal
from scipy.signal import find_peaks
import time
#import operator

def __abs__(self):
    return (self.x ** 2 + self.y ** 2) ** 0.5

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


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
filename1 = 'RA_ascend.csv'
csv1 = np.genfromtxt (filename1, delimiter=",")
second = csv1[1,:]
third = csv1[2,:]

#print(csv1[:,1])
xraw1 = csv1[:,0]
yraw1 = csv1[:,1]
#yraw1 = yraw1 - 2000
plt.plot(xraw1,yraw1, 'o')


filename2 = 'RA_descend.csv'
csv2 = np.genfromtxt (filename2, delimiter=",")
second2 = csv2[1,:]
third2 = csv2[2,:]

xraw2 = csv2[:,0]
yraw2 = -1*csv2[:,1]
#yraw2 = csv2[:,1]
#yraw2 = -1*(yraw2-2000)
plt.plot(xraw2,yraw2, 'o')

#plt.show()


# =============================================================================
# fig1, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
# ax1.xcorr(csv1[:,1], csv2[:,1], usevlines=True, maxlags=35, normed=True, lw=2)
# ax1.grid(True)
# 
# ax2.acorr(csv1[:,1], usevlines=True, normed=True, maxlags=35 , lw=2)
# ax2.grid(True)
# =============================================================================




#alternate interpolation method
#f1 = InterpolatedUnivariateSpline(xraw1, yraw1)
#f2 = InterpolatedUnivariateSpline(xraw2,yraw2)

#f1 = interp1d(xraw1, yraw3, kind='cubic') #interpolation to 1 sample/ms
#f2 = interp1d(xraw2, yraw4, kind='cubic')#csv2[:,1], kind='cubic')

ab = max(csv1[:,0])
abc = 1000 * (ab + 1)
abcd = int(abc)
csvxnew = np.linspace(0, max(csv1[:,0]), abcd, endpoint=True) #adjust x scale to accomodate
#csvxnew = np.arange(abc)

x = csv1[:,0]
y = csv1[:,1]
yraw3 = [0] * len(yraw1)
yraw4 = [0] * len(yraw2)
#y3 = [0] * len(y1)
#y4 = [0] * len(y2)

for i in range(len(yraw1)):
    yraw3[i] = (yraw1[i] - min(yraw1)) / (max(yraw1) - min(yraw1))
    
print("Checkpoint1")
t1 = time.time()
total = t1-t0
print('Time elapsed: ', total, 's')

for i in range(len(yraw2)):
    yraw4[i] = (yraw2[i] - min(yraw2)) / (max(yraw2) - min(yraw2))


my1 = max(yraw3)
my2 = max(yraw4)

TT_method = input("Please choose a FTF method 20, 25 or 50: ")

FTF_method = int(float(TT_method))

if FTF_method == 20:
    print("20% FTF Selected")
    half1 = 0.20*my1
    half2 = 0.20*my2

elif FTF_method == 25:
    print("25% FTF Selected")
    half1 = 0.25*my1
    half2 = 0.25*my2

elif FTF_method == 50:
    print("50% FTF Selected")
    half1 = 0.50*my1
    half2 = 0.50*my2 

else:
    print("Invalid Value")   
    
#print("50% Selected")
#half1 = 0.50*my1
#half2 = 0.50*my2

nhalf1 = find_nearest(yraw3, half1)
nhalf2 = find_nearest(yraw4, half2)

my1loc = np.where(yraw3 == nhalf1)#y1.index(half1)
my2loc = np.where(yraw4 == nhalf2) #y2.index(half2)
#TA = csvxnew[my1loc] #csvxnew[]
#TD = csvxnew[my2loc]
TA = xraw1[my1loc]
TD = xraw2[my2loc]
print(TA)
print(TD)
TT = TA - TD
TT2 = TD - TA
#distance = math.sqrt( ((TA-TD)**2)+((nhalf1-nhalf2)**2) )

print('TT TA-TD: ', TT)
print()
print('TT TD-TA: ', TT2)
print()
#print('Distance: ', distance)
print()
