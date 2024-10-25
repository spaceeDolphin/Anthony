import numpy as np
import matplotlib.pyplot as plt

def R(t):
    return np.sqrt(2)*a*np.sqrt(np.cos(3*t))
    #return a*np.cos(20*t)

def Kx(r,t):
    return r*np.cos(t)

def Ky(r,t):
    return r*np.sin(t)

a=2
tValues=np.linspace(0,2*np.pi,10000)
rValues=R(tValues)
xValues=Kx(rValues,tValues)
yValues=Ky(rValues,tValues) 

plt.plot(xValues,yValues)
