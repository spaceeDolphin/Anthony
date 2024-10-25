import matplotlib.pyplot as plt
import numpy as np
from math import comb

def Binominal(n,x,p):
    return comb(n,x) * p**x * (1-p)**(n-x)

def Geo(y,p):
    return (1-p)**(y-1) * p

def Hypergeo(N,M,n,x):
    return comb(M,x) * comb(N-M,n-x) / comb(N,n)

def Poisson(l,k):
    kFak = 1
    for j in range(1,k+1):
        kFak = kFak * j
    return (np.exp(-l) * l**k) / kFak

n=120
N=25
M=9
p=0.08
l=5
xValues = np.linspace(0,n,n+1)
pValues = np.zeros(n+1)


for i in range(n+1):
    pValues[i] = Binominal(n,i,p)
    #pValues[i] = Hypergeo(N,M,n,i)
    #pValues[i] = Geo(i,p)
    #pValues[i] = Poisson(l,i)

plt.bar(xValues,pValues,color="green")
print(sum(pValues[1:4]))