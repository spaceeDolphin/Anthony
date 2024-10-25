import numpy as np
import matplotlib.pyplot as plt

def Pt100(T):
    return 100*(1+0.003908*T)

def Vb(T):
    return E*((R2/(R1+R2))-(Pt100(T)/(R3+Pt100(T))))
    
R1=97600
R3 = R1
R2=100
E=10
n=26

tc25=-1
tc50=-2.023
vb0=Vb(0)*1000
vb25=Vb(25)*1000

print(tc25,vb0,tc25+vb0)
print(tc25,round(vb25,2),round(tc25+vb25,2))
print(tc50,vb0,tc50+vb0)
print(tc50,round(vb25,2),round(tc50+vb25,2))

tValues=np.linspace(0,25,n)
vbValues=(Vb(tValues))
tcValues=np.zeros(n)
for i in range(n):
    tcValues[i]=-i*0.000039

plt.plot(tValues,vbValues)
plt.plot(tValues,tcValues)
plt.xlabel("T [C]")
plt.ylabel("Vb [V]")

print("0 grader C: ",Pt100(0))
print("20 grader C: ",Pt100(20))
print("100 grader C: ",Pt100(100))