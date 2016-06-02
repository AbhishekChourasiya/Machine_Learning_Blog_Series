# script – 4
# it is in continuity with previous code 
divider = 400
xa = x[: divider]
ya = y[: divider]
xb = x[divider :]
yb = y[divider :]

## fit two lines to two datasets
fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))
fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)
print("Error using partition: %f"% (fa_error + fb_error))
plt.plot(fx[: divider], fa(fx[: divider]), linewidth = 4, label = ("d = 1+"), color = "orange")
plt.plot(fx[divider: ], fb(fx[divider :]), linewidth = 4, label = ("d = 1+"), color = "orange")

plt.legend(loc = "upper left")
plt.show()
