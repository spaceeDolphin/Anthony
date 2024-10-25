import numpy as np
import matplotlib.pyplot as plt
import timeit as time

def f(x):
    return np.sin(x)

# FEILESTIMERING
def ddf(x):
    return abs(-np.sin(x))
feilestimering = True
m2 = 0

# PARAMETERS
n = 100
a = 0
b = 2*np.pi

dx = (b-a)/n
sumØvre = 0
sumNedre = 0
sumMiddel = 0

# PLOTTING
plotNedre = False
plotØvre = False
plotMiddel = False
plot = False

plotInput = 'md' #input("Plot? n: nei, nd: nedre, øv: øvre, md: middel")
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
    zeros = np.zeros(n)
    fig, func = plt.subplots()

for i in range(n):
    xNedre = a + (dx*i)
    fNedre = f(xNedre)
    xØvre = a + dx*(i+1)
    fØvre = f(xØvre)
    xMiddel = xNedre + dx/2
    fMiddel = f(xMiddel)
    
    delsumNedre = dx * fNedre
    delsumØvre = dx * fØvre
    delsumMiddel = dx * fMiddel
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
            yValues[i] = fNedre
            func.add_patch(plt.Rectangle((xNedre,0), dx, fNedre, facecolor = color))
        elif plotØvre:
            yValues[i] = fØvre
            func.add_patch(plt.Rectangle((xNedre,0), dx, fØvre, facecolor = color))
        elif plotMiddel:
            yValues[i] = fMiddel
            func.add_patch(plt.Rectangle((xNedre,0), dx, fMiddel, facecolor = color))
    
    sumNedre += delsumNedre
    sumØvre += delsumØvre
    sumMiddel += delsumMiddel

if feilestimering:
    error = (m2*(b-a)**3)/(24*n**2)
    print("Error, midtpunkt:", error)

if plot: 
    if (min(yValues) < 0):
        plt.ylim(min(yValues) + min(yValues)*0.1, max(yValues) + max(yValues)*0.1)
    else:
        plt.ylim(0, max(yValues) + max(yValues)*0.1)
    plt.ylim
    plt.plot(xValues, zeros, "k.")
    plt.plot(xValues, yValues, "ro--")
    plt.grid()
    plt.show()

snittØvreNedre = sumNedre + (sumØvre - sumNedre)/2
    
print("Nedre Sum =", round(sumNedre, 2))
print("Øvre Sum =", round(sumØvre, 2))
print("Middel Sum =", round(sumMiddel, 2))
print("Snitt Sum =", round(snittØvreNedre, 2))

timeStop = time.default_timer()
print("RUNTIME:", timeStop - timeStart)