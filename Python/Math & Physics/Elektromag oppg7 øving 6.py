import numpy as np
import matplotlib.pyplot as plt

def c(h,er):
    e0 = 8.85*10**(-12)
    H = 0.2
    R = 0.018
    r = 0.0067
    k = 2*np.pi*e0*H / np.log(R/r)
    c = k * (1 + (h/H)*(er-1))
    return c

erWater = 80
erOil = 2.3
n = 1000
hValues = np.linspace(0,0.2,n)
cValues = c(hValues,erWater)
aValues = np.linspace(4,20,n)

print("Tom tank = ", cValues[0], "Farad")
print("Full tank = ", cValues[n-1], "Farad")

level370pF = 0
for i in range(n):
    if cValues[i] < 370 * 10**(-12):
        level370pF = hValues[i]
        
print("Ved h =",round(level370pF,3),"m, er kapasitansen 370 pF")

cOil83mm = c(0.083, erOil)
cWater83mm = c(0.083, erWater)
print("Kapasitans ved 83mm olje med permittivitet 2.3 =", cOil83mm)
print("Kapasitans ved 83mm vann med permittivitet 80 =", cWater83mm)

level12mA = 0
for i in range(n):
    if aValues[i] < 12:
        level12mA = hValues[i]
        
print("Nivå ved 12mA er", round(level12mA,3), "m")

plt.plot(hValues, cValues, "g-", label="C tot som funksjon av h")
plt.grid()
plt.xlabel("væskenivå h[m]")
plt.ylabel("kapasitans C[F]")
plt.legend()
plt.show()
    
