import numpy as np
import matplotlib.pyplot as plt
import timeit as time

def f(x):
    return np.sin(x)

def g(x):
    return np.cos(3*x)

# FEILESTIMERING
def ddf(x):
    return abs(-np.sin(x))
feilestimering = True
m2 = 0

# PARAMETERS
n = 1000
a = 0
b = 10

dx = (b-a)/n
sumØvre = 0
sumNedre = 0
sumMiddel = 0

# PLOTTING
plotNedre = False
plotØvre = False
plotMiddel = False
plot = False

plotInput = "md" #input("Plot? n: nei, nd: nedre, øv: øvre, md: middel")
if plotInput != "n":
    plot = True
    if plotInput == "nd":
        plotNedre = True
    elif plotInput == "øv":
        plotØvre = True
    elif plotInput == "md":
        plotMiddel = True

timeStart = time.default_timer()

if plot:
    if plotNedre:
        xValues = np.arange(a, b, dx)
    elif plotØvre:
        xValues = np.arange(a+dx, b+dx, dx)
    elif plotMiddel:
        xValues = np.arange(a+dx/2, b+dx/2, dx)
        
    yValues = np.zeros(n)
    zValues = np.zeros(n)
    zeros = np.zeros(n)
    fig, func = plt.subplots()

for i in range(n):
    xNedre = a + (dx*i)
    fNedre = f(xNedre)
    gNedre = g(xNedre)
    dNedre = abs(fNedre - gNedre)
    
    xØvre = a + dx*(i+1)
    fØvre = f(xØvre)
    gØvre = g(xØvre)
    dØvre = abs(fØvre - gØvre)
    
    xMiddel = xNedre + dx/2
    fMiddel = f(xMiddel)
    gMiddel = g(xMiddel)
    dMiddel = abs(fMiddel - gMiddel)
    
    delsumNedre = dx * dNedre
    delsumØvre = dx * dØvre
    delsumMiddel = dx * dMiddel
    #print("x =", xNedre, "Delsum =", delsumNedre)
    
    if feilestimering:
        if (m2 < ddf(xMiddel)):
            m2 = ddf(xMiddel)
            
    if plot:
        if i % 2 == 0:
            color = "seagreen"
        else: 
            color = "springgreen"
        
        if plotNedre:
            if gNedre < fNedre:
                hNedre = gNedre
            else:
                hNedre = fNedre
                
            yValues[i] = fNedre
            zValues[i] = gNedre
            func.add_patch(plt.Rectangle((xNedre,hNedre), dx, dNedre, facecolor = color))
        elif plotØvre:
            if gØvre < fØvre:
                hØvre = gØvre
            else:
                hØvre = fØvre
                
            yValues[i] = fØvre
            zValues[i] = gØvre
            func.add_patch(plt.Rectangle((xNedre,hØvre), dx, dØvre, facecolor = color))
        elif plotMiddel:
            if gMiddel < fMiddel:
                hMiddel = gMiddel
            else:
                hMiddel = fMiddel
                
            yValues[i] = fMiddel
            zValues[i] = gMiddel
            func.add_patch(plt.Rectangle((xNedre,hMiddel), dx, dMiddel, facecolor = color))
    
    sumNedre += delsumNedre
    sumØvre += delsumØvre
    sumMiddel += delsumMiddel

if feilestimering:
    error = (m2*(b-a)**3)/(24*n**2)
    print("Error, midtpunkt:", error)

if plot:    
    #plt.ylim(min(yValues) + min(yValues)*0.1, max(yValues) + max(yValues)*0.1)
    plt.plot(xValues, zeros, "k.")
    plt.plot(xValues, yValues, "r.--")
    plt.plot(xValues, zValues, "m.--")
    plt.show()

snittØvreNedre = sumNedre + (sumØvre - sumNedre)/2
    
print("Nedre Sum =", round(sumNedre, 2))
print("Øvre Sum =", round(sumØvre, 2))
print("Middel Sum =", round(sumMiddel, 2))
print("Snitt Sum =", round(snittØvreNedre, 2))

timeStop = time.default_timer()
print("RUNTIME:", timeStop - timeStart)