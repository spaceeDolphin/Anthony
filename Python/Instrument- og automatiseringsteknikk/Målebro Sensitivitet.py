import numpy as np
import matplotlib.pyplot as plt

def R(T):
    return 100.0*(1 + 0.003908*T)

def S(R1):
    return (R1/(R1 + R(T))**2)*E

E=10
T=20
rValues=np.linspace(0,500,1000)
yValues=np.zeros(1000)
yMax = 0
yMaxIndex = 0

for i in range(1000):
    sen = S(rValues[i])
    yValues[i] = sen
    if sen > yMax:
        yMax = sen
        yMaxIndex = i
    
plt.plot(rValues,yValues)
plt.grid()

print(rValues[yMaxIndex],"ohm")
