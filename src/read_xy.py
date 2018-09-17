import numpy as np
import matplotlib.pyplot as plt

x=[]
y=[]
filepath="../data/xy.dat"

with open(filepath,"r") as f:
    for line in f:
        x_,y_=np.array(line.split(),dtype=float)
        x.append(x_)
        y.append(y_)

x = np.array(x)
y = np.array(y)

plt.plot(x, y)
plt.show()
