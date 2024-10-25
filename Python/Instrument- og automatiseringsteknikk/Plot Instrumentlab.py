import pandas as pd
import numpy as np
data = pd.read_csv('C:/Users/antho/OneDrive/Dokumenter/Python Scripts/Python Files/project/arduinomes2.txt',sep='\t',header=None)
data = pd.DataFrame(data)

import matplotlib.pyplot as plt
#x = data[0][50:200]
#y = data[1][50:200]
x = np.array([25,50,100,50,25])
y = np.array([127,177,413,259,131])
xRef = np.array([25,50,100])
#yRef = np.array([3.7*25,3.7*100])
#yRef = xRef * 3.7 + 34.5
yRef = xRef * 3.787 + 34
zRef = xRef *   3.94 + 32

#223.5 mV ved 50C

plt.figure(dpi=400)
plt.plot(x, y,'r-', label="Kalibreringskarakteristikk")
plt.plot(xRef, yRef, "k--", label="Referansekarakteristikk")
plt.plot(xRef, zRef, "m--", label="Beregnet karakteristikk")
#plt.plot(np.array([50,50]),np.array([259,yRef[1]]),"g--",label="Største Avvik")
plt.plot()
plt.xlabel("[deg C]")
plt.ylabel("[mV]")
plt.grid()
plt.legend()
#plt.tick_params(labelcolor='r', labelsize='medium', width=3)
plt.show()

