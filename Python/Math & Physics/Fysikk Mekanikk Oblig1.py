import numpy as np 
import matplotlib.pyplot as plt 
 
h0 = 50 
v0 = 0 
m = 0.1 
g = 9.81 
C = 0.05 
 
impact = -1 
impactNoAir = -1 
 
N = 10000
tmin = 0 
tmax = 12 
 
times = np.linspace(tmin, tmax, N) 
dt = times[1] - times[0]            # Delta t 
 
h = np.zeros(N) 
v = np.zeros(N) 
a = np.zeros(N) 
 
hNoAir = np.zeros(N) 
vNoAir = np.zeros(N) 
 
h[0] = h0 
v[0] = v0 
a[0] = g 
 
hNoAir[0] = h0 
vNoAir[0] = v0 
 
def air(vel): 
    return (C*vel**2)/m 
 
 
for i in range(1, N): 
    v[i] = v[i-1] + a[i-1]*dt 
    h[i] = h[i-1] - v[i-1]*dt 
    a[i] = g - air(v[i]) 
     
    if ((h[i] <= 0) and (impact == -1)): 
        impact = times[i] 
        print("Kula traff bakken etter", round(times[i],3), "sekunder, med luftmotstand") 
        print("Da hadde kula hastighet", round(v[i],3), "m/s") 
 
     
for i in range(1, N): 
    vNoAir[i] = vNoAir[i-1] + g*dt 
    hNoAir[i] = hNoAir[i-1] - vNoAir[i-1]*dt 
     
    if ((hNoAir[i] <= 0) and (impactNoAir == -1)): 
        impactNoAir = times[i] 
        print("Kula traff bakken etter", round(times[i],3), "sekunder, uten luftmotstand") 
        print("Da hadde kula hastighet", round(vNoAir[i],3), "m/s") 
         
         
figH = plt.figure(1) 
plt.ylim(0, 1.1*h0) 
K1, K2 = plt.plot(times, h, 'b', times, hNoAir, 'r--') 
figH.legend((K1, K2), ('Med luftmotstand', 'Uten luftmotstand'), 'upper right') 
plt.xlabel('t (sekunder)') 
plt.ylabel('h (meter)') 
plt.show() 
 
figV = plt.figure(2) 
plt.ylim(0, 1.1*vNoAir[N-1]) 
K1, K2 = plt.plot(times, v, 'b', times, vNoAir, 'r--') 
figV.legend((K1, K2), ('Med luftmotstand', 'Uten luftmotstand'), 'upper right') 
plt.xlabel('t (sekunder)') 
plt.ylabel('v (m/s)') 
plt.show() 