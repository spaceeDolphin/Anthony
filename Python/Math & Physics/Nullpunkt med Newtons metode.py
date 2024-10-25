#%% Newtons metode
import numpy as np
import matplotlib.pyplot as plt

#Løser likningen sin(2x)=x

def f(x):
    return np.sin(2*x) - x  

def dfdx(x):
    return 2*np.cos(2*x) - 1

#x0
x = 8
n = 20
i = 0

plt.grid()
"""
for i in range(n):
    x -= f(x)/dfdx(x)
    print(x)
    plt.plot(x, f(x), "go--")"""

while (np.abs(f(x)) > 10**(-6) and i <1000 ):
    x -= f(x)/dfdx(x)
    print(x)
    i += 1
    plt.plot(x, f(x), "go--")
