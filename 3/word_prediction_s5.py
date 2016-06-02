# script - 5
# entirely independent code
import scipy as sp
import numpy as np

data = sp.genfromtxt("ML_curve_fitting_example.dat", delimiter = "\t")
print("Last 10 rows: " + str(data[-10:]))#print last 10 items in our dataset
print(data.shape)

## separate data in two different lists
x = data[:, 0]
y = data[:, 1]
print("y min = " + repr(min(y)) + "\t y max = " + repr(max(y)))

y = sp.multiply(y, 100000)

#print(sp.sum(sp.isnan(y)))
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

train_data_len = 50
x_train = x[: (len(x) - train_data_len)]
y_train = y[: (len(y) - train_data_len)]
x_test = x[(len(x) - train_data_len) :]
y_test = y[(len(x) - train_data_len) :]

print("Training Set: %i"% len(x_train))
print("Test Set: %i"% len(x_test))

## lets plot something
importmatplotlib.pyplot as plt
plt.scatter(x_train, y_train)
plt.scatter(x_test, y_test)

## function: returns squared difference between function value and predicted value 
def error(f, x_train, y_train):
	returnsp.sum((f(x_train) - y_train) **2)

## function: plotting help, rather than repeatedly typing the same things, let us use a short-cut
defYearsVSUse():
	plt.title("Training and testing of usage of word \"artificial\" over 1500 to 1999")
	plt.xlabel("Years")
	plt.axis([0, 500, 0, 10])
	plt.ylabel("Score of use")
	plt.grid()

fx = sp.linspace(0, x[-1], len(x))
fx_tr = fx[: (len(x) - train_data_len)]
fx_tst = fx[(len(x) - train_data_len) :]

## First order polynomial fitted to data
fp1, residuals, rank, sv, rcond = sp.polyfit(x_train, y_train, 1, full = True)
#print("Res: " + str(residuals))
#print("Model parameters: %s" % fp1)
f1 = sp.poly1d(fp1)
print("Error O_1: " + str(error(f1, x_train, y_train) ))
plt.plot(fx_tr, f1(fx_tr), linewidth = 3, label = "d = %i"% f1.order, color = "blue")

## Second order polynomial fitted to data
f2p = sp.polyfit(x_train, y_train, 2)
#print("Model parameters: %s" % f2p)
f2 = sp.poly1d(f2p)
print("Error O_2: " + str(error(f2, x_train, y_train) ))
plt.plot(fx_tr, f2(fx_tr), linewidth = 3, label = "d = %i"% f2.order, color = "red")

## Third order polynomial fitted to data
f3p = sp.polyfit(x_train, y_train, 3)
#print(" Model parameters: %s" % f3p)
f3 = sp.poly1d(f3p)
print("Error O_3: " + str(error(f3, x_train, y_train) ))
plt.plot(fx_tr, f3(fx_tr), linewidth = 3, label = "d = %i"% f3.order, color = "green")

## Tenth order polynomial fitted to data
f10p = sp.polyfit(x_train, y_train, 10)
#print("Model parameters: %s" % f10p)
f10 = sp.poly1d(f10p)
print("Error O_10: " + str(error(f10, x_train, y_train) ))
plt.plot(fx_tr, f10(fx_tr), linewidth = 3, label = "d = %i"% f10.order, color = "yellow")

## Fiftieth order polynomial fitted to data
f50p = sp.polyfit(x_train, y_train, 50)
f50 = sp.poly1d(f50p)
print("Error O_50: " + str(error(f50, x_train, y_train)))
plt.plot(fx_tr, f50(fx_tr), linewidth = 3, label = "d = %i"% f50.order, color = "orange")

YearsVSUse()

print("test: order_1 = %f"% error(f1, x_test, y_test))
print("test: order_2 = %f"% error(f2, x_test, y_test))
print("test: order_3 = %f"% error(f3, x_test, y_test))
print("test: order_10 = %f"% error(f10, x_test, y_test))
print("test: order_50 = %f"% error(f50, x_test, y_test))

## plot the fitted values against test data
plt.plot(fx_tst, f1(fx_tst), linewidth = 3, label = "d = %i"% f1.order, color = "blue")
plt.plot(fx_tst, f2(fx_tst), linewidth = 3, label = "d = %i"% f2.order, color = "red")
plt.plot(fx_tst, f3(fx_tst), linewidth = 3, label = "d = %i"% f3.order, color = "green")
plt.plot(fx_tst, f10(fx_tst), linewidth = 3, label = "d = %i"% f10.order, color = "yellow")
plt.plot(fx_tst, f50(fx_tst), linewidth = 3, label = "d = %i"% f50.order, color = "orange")

YearsVSUse()
plt.legend(loc = "upper left")
plt.show()

fromscipy.optimize import fsolve
becomes_ancient_at = fsolve(f3, 500)
print("Word \"artificial\" will become ancient in: " + str(becomes_ancient_at[0] + 1500.0))
