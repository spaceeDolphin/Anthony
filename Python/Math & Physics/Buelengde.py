import numpy as np
import matplotlib.pyplot as plt

def lengde(x,y):
    return np.sqrt(x**2 + y**2)

def f(x):
    return x**3/12 + 1/x

# FEILESTIMERING f''
def ddf(x):
    return abs(2/x**3)

# PARAMETERS
n = 1000
a = 1
b = 4

dx = (b-a)/n
sumLengde = 0
xValues = np.arange(a,b+dx,dx)
yValues = f(xValues)

# FEILESTIMERING
m2 = max(ddf(xValues))
error = (m2*(b-a)**3)/(24*n**2)
print("Feil:",error)

for i in range(1,n+1):
    dy = yValues[i] - yValues[i-1]
    dl = lengde(dx,dy)
    #print(dl)
    sumLengde += dl
    
plt.figure(1)
if (min(yValues) < 0):
    plt.ylim(min(yValues) + min(yValues)*0.1, max(yValues) + max(yValues)*0.1)
else:
    plt.ylim(0, max(yValues) + max(yValues)*0.1)
plt.plot(xValues, yValues, "k.-")
plt.show() 

print("Buelengde =", round(sumLengde, 2))

    