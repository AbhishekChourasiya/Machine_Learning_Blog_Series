# script - 2
# it is assumed that previously demonstrated code is present

## function: returns squared difference between function value and predicted value
def error(f, x, y):
	return sp.sum((f(x) - y) **2)

## generate 'x' values for our function
fx = sp.linspace(0, x[-1], len(y))

fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full = True)
print(“Res: ” + str(residuals))
print("Model parameters: %s" % fp1)
f1 = sp.poly1d(fp1)
print(“Error O_1: ” + str(error(f1, x, y)) )

## let us plot our line 
plt.plot(fx, f1(fx), linewidth = 3, label = "d = %i"% f1.order)
plt.show()
