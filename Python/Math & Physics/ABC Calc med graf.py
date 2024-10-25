import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 5.6e-10
c = -0.015*b

def f(x,a,b,c):
    return (a*(x**2)) + (b*x) + c

test = b**2 - 4*a*c

if test > 0:
    l1 = ((-b + np.sqrt(test))/(2*a))
    l2 = ((-b - np.sqrt(test))/(2*a))
    
    if l1 > l2:
        x = np.linspace(l2, l1, 100)
    else:
        x = np.linspace(l1, l2, 100)
    
    y = f(x,a,b,c)

    plt.plot(x, y)
    plt.grid()
    print("to løsning", l1, l2)
elif test == 0:
    l1 = -b/(2*a)
    x = np.linspace(l1-1, l1+1, 100)
    plt.plot(x, f(x,a,b,c))
    plt.grid()
    print("en løsning")
    
else:
    print("ingen løsning")
    
#%%

def S(t):
    return -0.01*(t**3) + 0.255*(t**2) - 0.48*(t) + 5

print(S(0))
print(S(1))
print(S(16))
print(S(24))


#%%

x = 10**(-3.2)
ka = 1.78e-04
c1 = x**2/ka + x

print(c1)



















