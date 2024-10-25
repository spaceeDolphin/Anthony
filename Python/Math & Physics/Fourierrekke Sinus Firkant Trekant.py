import numpy as np
import matplotlib.pyplot as plt

def sinus(x,n):
    return (1/n)*np.sin(n*x)

ns = 1000         #Antall n-verdier, antall sinuskurver som legges sammen
start = 0
stop = 10
xVals = 1000
firkant = False
showAllHarmonic = True

xValues = np.linspace(start, stop, xVals)
yValues = np.zeros(xVals)
if (firkant):
    nValues = np.arange(1, 2*ns, 2)
else:
    nValues = np.arange(1, ns+1)

for n in nValues:
    iValues = sinus(xValues,n)
    yValues += iValues
    if (showAllHarmonic):
        plt.plot(xValues, iValues)
    
plt.plot(xValues, yValues, "k-")

#%% Fourier
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

def Get_a0():
    iSum = 0
    for x in piValues:
        iSum += f(x)*dx
    return iSum * 1/(2*np.pi)

def Get_an(n):
    iSum = 0
    for x in piValues:
        iSum += f(x)*np.cos(n*x)*dx
    return iSum / np.pi

def Get_bn(n):
    iSum = 0
    for x in piValues:
        iSum += f(x)*np.sin(n*x)*dx
    return iSum / np.pi

def F(x,n):
    return (Get_an(n) * np.cos(n*x)) + (Get_bn(n) * np.sin(n*x))

# Teste eksempeloppgave med utregning
def F1(x,n):
    return 0.5 + ((6/np.pi) * (1/((2*n)+1) * np.sin((2*n + 1) * np.pi * x / 2)))
    #return  0.5 + (6/(2-4*n)) * np.sin((2*n+1)*np.pi*x / 2)

k = 10
N = 1000
xLow = -2
xHigh = 2
xValues = np.linspace(xLow,xHigh, N)
# OBS kun mulig i periode 2pi

# Finding a0, an, bn
piValues = np.linspace(-np.pi, np.pi, N)
dx = 2*np.pi/N
a0 = Get_a0()
print(a0)

# Original funksjon f(x)
yValues = f(xValues)
#plt.plot(xValues, yValues)

# Tester fourierrekke funnet ved regning
zValuesManual = np.zeros(N)
for i in range(1,k):
    zValuesManual += F1(xValues, i)
plt.plot(xValues, zValuesManual)

# Tester fourierrekke funnet ved numerisk iterasjon
zValues = np.ones(N) * a0
for i in range(1,k):
    zValues += F(xValues, i)
    
#plt.plot(xValues, zValues)




























