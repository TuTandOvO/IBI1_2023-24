uk_cities=[0.56,0.62,0.04,9.7]#a list of the size of UK cities
China_cities=[0.58,8.4,29.9,22.2]#a list of the size of China cities 
import numpy as py#import python tools 
import matplotlib.pyplot as plt#import python tools 
x = ["Edinburgh","Glasgow","Stirling","London"]#x serves as names of UK cities
y = uk_cities#y serves as the size of UK cities
a = ["Haining","Hangzhou","Shanghai","Beijing"]#a serves as names of China cities
b = China_cities#b serves as the size of China cities
plt.figure()
plt.barh(x,y)#use the barh graph included in the matplotlib
plt.figure()#show the figure in the second window
plt.barh(a,b)
plt.show()#show the graph in a new window
plt.clf()