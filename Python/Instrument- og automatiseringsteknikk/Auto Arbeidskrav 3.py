import numpy as np
import matplotlib.pyplot as plt
    
def PIControl(tankLevel, tankSetPoint, Kc, Ti, Ts, u_i, u_man):
    u_max = 1 # pumpe pådrag 0 = 0%, 1 = 100%
    u_min = 0
    Imax = 1
    
    error = tankLevel - tankSetPoint
    P = Kc * error
    I = u_i + ((Kc/Ti)*Ts*error)
    
    # Anti-windup
    if I > Imax:
        I = Imax
    elif I < -Imax:
        I = -Imax
        
    u = u_man + P + I
    
    if u > u_max:
        u = u_max
    elif u < u_min:
        u = u_min
    
    return u, I

def InFlow(t, amplitude, periodTime):
    #if t < 2000:
    #    return 3
    #elif t >= 2000:
    #    return 2
    return amplitude + amplitude * np.sin(2*np.pi*(1/periodTime)*t)

# PARAMETERS
# The tank
tankSurface = 2000 # m2
tankHeight = 2 # m
tankSetPoint = 1 # m
tankSetPointVolume = tankSurface * tankSetPoint # m3
tankSetPointFraction = tankSetPoint/tankHeight # %
tankLevel = 1 # m
tankLevelVolume = tankSurface * tankLevel # m3
tankLevelFraction = tankLevel/tankHeight # %

# Simulation
timeSim = 10000 # s
timeSample = 1 # s
timeValues = np.linspace(0,timeSim,int(timeSim/timeSample)) # for plotting

# Plot Tank Values
tankSetPointValues = np.ones(int(timeSim/timeSample)) * tankSetPoint
tankValues = np.zeros(int(timeSim/timeSample))
tankValues[0] = tankLevel

# Inflow
amplitude = 1 # m3/s
periodTime = 200 # s

# Regulator
Kc = 2
Ti = 2000 # s
Ikm1 = 0 # last iteration of integral in PI-regulator
uMan = (1/5) # min 0, max 1

# OutFlow
flowOutMax = 5 # m3/s

# Plot Flow
flowInValues = np.zeros(int(timeSim/timeSample))
flowOutValues = np.zeros(int(timeSim/timeSample))
flowInValues[0] = InFlow(0, amplitude, periodTime)
flowOutValues[0] = uMan*flowOutMax

for t in range(1, timeSim):
    flowOutFraction, Ikm1 = PIControl(tankLevelFraction, tankSetPointFraction, Kc, Ti, timeSample, Ikm1, uMan)
    flowIn = InFlow(t, amplitude, periodTime)
    flowOut = flowOutMax * flowOutFraction * timeSample
    tankLevelVolume += flowIn
    tankLevelVolume -= flowOut
    tankLevel = tankLevelVolume/tankSurface
    tankLevelFraction = tankLevel/tankHeight
    
    if tankLevel < 0:
        tankLevel = 0
    tankValues[t] = tankLevel
    
    # Plot Flow
    flowInValues[t] = flowIn
    flowOutValues[t] = flowOut

# Amplitude Flow Analysis
flowHigh = max(flowOutValues[000:10000])
flowLow = min(flowOutValues[000:10000])
print(flowHigh, flowLow)
print((flowHigh - flowLow)/2)

# Plot Tank
#plt.plot(timeValues, tankValues, label="Tank Levels [m]")
#plt.plot(timeValues, tankSetPointValues, "g-", label="Set point [m]")
#plt.ylim(0,2)
#plt.ylabel("h [m]")

# Plot Flow
plt.plot(timeValues, flowInValues, "k-", label="Flow in [m3/s]")
plt.plot(timeValues, flowOutValues, "r-", label="Flow out [m3/s]")
#plt.ylim(0,5)
plt.ylabel("F [m3/s]")

plt.grid()
plt.xlabel("t [s]")
plt.legend()
plt.show()