import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    if x**2 + y**2 > 1:
        return 0
    else:
        return np.sqrt(1-x**2-y**2)

n = 100
xValues = np.linspace(-1, 1, n)
yValues = np.linspace(-1, 1, n) 
zValues = np.zeros((n,n))

plt.xlim(-1,1)
plt.ylim(-1,1)
plt.axis("equal")

for i in range(n):
    for j in range(n):
        x = xValues[i]
        y = yValues[j]
        h = f(x,y)
        zValues[i,j] = h
        if (h / 0.25 < 1.1) and (h / 0.25 > 0.9):
            plt.plot(x,y, "g.")
        if (h / 0.5 < 1.1) and (h / 0.5 > 0.9):
            plt.plot(x,y, "r.")
        if (h / 0.75 < 1.1) and (h / 0.75 > 0.9):
            plt.plot(x,y, "b.")

#%%

def fun():
    return 5
    return 7

var1 = fun() 
