# Script - 1
import scipy as sp
import numpy as np

data = sp.genfromtxt("ML_curve_fitting_example.dat", delimiter = "\t")
print(data[-10:])		## print last 10 items in our dataset
print(data.shape)

## separate data in two different lists
x = data[:, 0]
y = data[:, 1]

## a quick statistic: min and max of word's score
print("y min = " + repr(min(y)) + "\t y max = " + repr(max(y)))

## as the range of score is too low, let is scale 
y = sp.multiply(y, 100000)

## if there are missing values, those have to be taken care of
#print(sp.sum(sp.isnan(y))) 
x = x[~sp.isnan(y)] # Be careful. This is not a typo. NaN will be present for score, not for years!
y = y[~sp.isnan(y)]

## lets plot something
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.title("Use of word \"artificial\" over 1500 to 1999")
plt.xlabel("Years")
plt.ylabel("Score of use")
axes = plt.gca()
axes.set_ylim([min(y), max(y)])
plt.autoscale(tight = True)
plt.grid()
plt.show()
