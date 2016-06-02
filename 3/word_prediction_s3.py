# script - 3
# it is assumed that previous code is present

## trying to fit second order polynomial
f2p = sp.polyfit(x, y, 2)
#print("Model parameters: %s" % f2p)
f2 = sp.poly1d(f2p)
print("Error O_2: " + str(error(f2, x, y) ))
plt.plot(fx, f2(fx), linewidth = 3, label = "d = %i"% f2.order)

## trying to fit third order polynomial
f3p = sp.polyfit(x, y, 3)
#print(" Model parameters: %s" % f3p)
f3 = sp.poly1d(f3p)
print("Error O_3: " + str(error(f3, x, y) ))
plt.plot(fx, f3(fx), linewidth = 3, label = "d = %i"% f3.order)

## trying to fit tenth order polynomial
f10p = sp.polyfit(x, y, 10)
#print("Model parameters: %s" % f10p)
f10 = sp.poly1d(f10p)
print("Error O_10: "+ str(error(f10, x, y) ))
plt.plot(fx, f10(fx), linewidth = 3, label = "d = %i"% f10.order)

## trying to fit hundredth order polynomial
f100p = sp.polyfit(x, y, 100)
f100 = sp.poly1d(f100p)
print("Error O_100: " + str(error(f100, x, y)))
plt.plot(fx, f100(fx), linewidth = 3, label = "d = %i"% f100.order)
plt.legend(loc = "upper left")
## plot all the polynomial's fittings
plt.show()
