import numpy as np
import matplotlib.pyplot as plt

# HOI, vannkokeren er kraftig modifisert med justerbart pådrag og regulering

# temperature change in kettle
def dTdt(T_k):
    return (Pd_k + G*(T_env - T_k))/C

# theoretical highest temperature with kettle power
def finalT(Pd_k):
    return (Pd_k/G) + T_env

def OnOffControl(T_in, T_sp, e_db, Pd_k):
    if T_in > T_sp + e_db:
        Pd_k = Pd_off
    elif T_in < T_sp - e_db:
        Pd_k = Pd_on
    return Pd_k

def PI_Control(T_in, T_sp, Kp, Ti, Pd_i):
    e = T_sp - T_in
    P = Kp*e
    I = Pd_i + ((Kp/Ti)*dt*e)
    
    #anti-windup
    if I > Pd_i_max:
        I = Pd_i_max
    elif I < -Pd_i_max:
        I = -Pd_i_max
    
    Pd_k = Pd_man + P + I
    
    #if-else for å hindre negativ effekt eller effekt over det som er mulig
    if Pd_k > Pd_on:
        Pd_k = Pd_on
    elif Pd_k < Pd_off:
        Pd_k = Pd_off
    return Pd_k, I

T_env = 20 # oC (enviroment temp)
C_water = 4184 # J/K heat capacity water
water = 0.4 # Liters in kettle
C = C_water * water
G = 2.34 # W/K thermal conductivity, plastic kettle

dt = 1 # sec
t_start = 0
t_stop = 4000
n = int((t_stop-t_start)/dt)+1

Pd_on = 1000 # W
Pd_off = 0
Pd_man = 100
Pd_i = 0
Pd_i_max = 100 #100 is good
Kp = 30 #30 is good
Ti = 50 #50 is good

T_min = 0 # oC
T_max = 100
T_sp = 100
e_db = 0.5 # oC dødgang
i_delay = 10 # forsinket måling pga varmekapasitet i komponent

# Initializing
T_k = T_env
Pd_k = Pd_on
# arrays
tValues = np.linspace(t_start, t_stop, n)
tempValues = np.zeros(n)
tempValues[0] = T_k
tempValues2 = np.zeros(n)
tempValues2[0] = T_k
temp_envValues = np.ones(n)*T_env

T_spValues = np.zeros(n)
T_spValues[0] = T_sp

finaltempValues = np.ones(n)*finalT(Pd_k)

# Make line to see curve better
lineX=np.array([0])
lineY=np.array([T_env])

for i in range(1, n):
    if i >= i_delay:
        Pd_k, Pd_i = PI_Control(tempValues[i-i_delay], T_sp, Kp, Ti, Pd_i)
        
    tempValues[i] = tempValues[i-1] + dTdt(tempValues[i-1])*dt
    
    if i > n/4:
        T_sp = 75
    if i > 2*n/4:
        T_sp = 50
    if i > 3*n/4:
        T_sp = 100
        
    T_spValues[i] = T_sp
    
    #if tempValues[i-1] >= T_max:
        #Pd_k = Pd_off
        # Line to see curve better
        #lineX=np.append(lineX, tValues[i])
        #lineY=np.append(lineY, T_max)
    #else:
        #Pd_k = Pd_on

# Initializing
T_k = T_env
Pd_k = Pd_on
T_sp = 100

for i in range(1, n):
    if i >= i_delay:
        Pd_k = OnOffControl(tempValues2[i-i_delay], T_sp, e_db, Pd_k)
        
    tempValues2[i] = tempValues2[i-1] + dTdt(tempValues2[i-1])*dt
        
    if i > n/4:
        T_sp = 75
    if i > 2*n/4:
        T_sp = 50
    if i > 3*n/4:
        T_sp = 100

    
#fig, (ax1, ax2) = plt.subplots(2, sharex=True)
#plt.plot(tValues,tempValues2,"y-")
plt.plot(tValues,tempValues,"r-")
plt.plot(tValues, temp_envValues, "g-")
plt.plot(tValues, finaltempValues, "k--")
plt.plot(tValues, T_spValues, "k--")
#plt.plot(lineX,lineY,"k-")
plt.ylim([T_min, T_max+10])
plt.xlabel("t [s]")
plt.ylabel("T [oC]")
plt.grid()