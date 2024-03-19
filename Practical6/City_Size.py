uk_cities=[0.56,0.62,0.04,9.7]
China_cities=[0.58,8.4,29.9,22.2]
import numpy as py
import matplotlib.pyplot as plt
x = ["Edinburgh","Glasgow","Stirling","London"]
y = uk_cities
a = ["Haining","Hangzhou","Shanghai","Beijing"]
b = China_cities
plt.barh(x,y)
plt.barh(a,b)
plt.show()
plt.clf()