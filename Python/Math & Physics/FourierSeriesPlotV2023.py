import numpy as np
import matplotlib.pyplot as plt

# Calculated fourier series
def f(t,n):
    jump = 2*n-1
    #jump = 2*n
    #jump = n
    amplitude = 6/(jump*np.pi)
    periodHalf = 2
    flip = -1
    return amplitude * np.sin(flip*np.pi*(1/periodHalf)*jump*t)

# The original function
def y(t):
    if t < 0:
        return 2
    else:
        return -1

# PARAMETERS
N=20
xLimLow = -2
xLimHigh = 2
displacement = 1/2
# 

# Add up and show fourier series
tValues = np.linspace(xLimLow, xLimHigh, 1000)
FValues = np.ones(1000) * displacement
for n in range(1,N+1):
    FIteration = f(tValues,n) 
    FValues += FIteration
    # Show each iteration
    #plt.plot(tValues,FIteration,"y-")
    
# Show original function
yValues = np.zeros(1000)
for i in range(1000):
    yValues[i] = y(tValues[i])
plt.plot(tValues,yValues,"k-")
    
# Show fourier series
plt.grid()
plt.plot(tValues,FValues,"r-")
#ax = plt.gca()
#ax.set_aspect('equal', adjustable='box')


