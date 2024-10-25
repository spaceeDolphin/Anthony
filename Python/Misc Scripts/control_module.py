import numpy as np
#import matplotlib.pyplot as plt

def VoltToCelsius(V,a,b):
    #voltage signal to temperature in celsius
    T=np.sqrt(V*a+b)**2
    return T

def Filter(Tf, Ts, T_in, T_mem):
    a=1/((Tf/Ts)+1)
    T_out = (1-a) * T_mem + a*T_in
    return T_out

def OnOffControl(T_in, T_sp, dz, u):
    if T_in < T_sp - dz:
        return 5
    elif T_in > T_sp:
        return 0
    else:
        return u
    
def Integrator(T_in, T_sp, Kp, Ti, Ts, u_i):
    Imax = 1
    
    T_e = T_sp - T_in
    I = u_i + ((Kp/Ti)*Ts*T_e)
    
    # Anti-windup
    if I > Imax:
        I = Imax
    elif I < -Imax:
        I = -Imax
        
    return I
    
def PIControl(T_in, T_sp, Kp, u_i, u_man):
    u_max = 5
    u_min = 0
    
    T_e = T_sp - T_in
    P = Kp * T_e
    u = u_man + P + u_i
    
    if u > u_max:
        u = u_max
    elif u < u_min:
        u = u_min
    
    return u

# testing voltage to temperature
#voltageValues = np.linspace(1,5,1000)
#tempValues = VoltToCelsius(voltageValues,12.5,-12.5)
#plt.plot(voltageValues,tempValues,"g-")
#plt.xlabel("[V]")
#plt.ylabel("[C]")
#plt.grid()