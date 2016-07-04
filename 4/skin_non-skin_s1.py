# part - 1
from matplotlib import pyplot as plt
from matplotlib import patches as mpatches
import numpy as np
import scipy as sp

data = sp.genfromtxt("skin_color_binary.dat", delimiter = "\t")
sp.random.shuffle(data)
data = np.array(data)
print("Last 10 rows of Data: \n" + str(data[-10:]))
print(data.shape)

Y = data[:, (len(data[0]) - 1)] #equivalent to data[:, 3], we just made it generic
print("Last 10 labels: \n" + str(Y[-10:]))

X = data[:, range(0, 3)]
print("last 10 attributes: \n" + str(X[-10:]))

def plotter(c, index, plt):
    label_colors = ["yellow" if value == 1 else "red" for value in Y[:500]]
    c.scatter(sp.arange(500), X[:500, index], c = label_colors )
    if index == 0:
    	c.set_xlabel("blue")
    elif index == 1:
    	c.set_xlabel("green")
    else:
    	c.set_xlabel("red")
    c.set_ylabel("pixel value")
    skin_patch = mpatches.Patch(color = "yellow", label = "skin")
    non_skin_patch = mpatches.Patch(color = "red", label = "non-skin")
    plt.legend(handles = [skin_patch, non_skin_patch], loc = "upper left")

fig = plt.figure()
r = fig.add_subplot(131)
plotter(r, 0, plt)

g = fig.add_subplot(132)
plotter(g, 1, plt)

b = fig.add_subplot(133)
plotter(b, 2, plt)
plt.show()
