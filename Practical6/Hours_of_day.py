import numpy as py #inport python tools
import matplotlib.pyplot as plt #import python tools
sleep = 8
classes = 6
study = 3.5
tv = 2
music = 1
other = 3.5
Average_day = {"Sleeping":sleep,"Classes":classes,"Studying":study,"TV":tv,"Music":music,"Other":other} #make a dictionary to record the data which can be changed by the variables
print(Average_day)
Hours_types = ["Sleeping","Classes","Studying","TV","Music","Other"] #make a list of types of hours spending
Hours = [sleep,classes,study,tv,music,other] #make a list of hours spending variables
plt.pie(Hours, labels = Hours_types,autopct='%1.1f%%') #use pie graph that is included in the matplotlib
plt.show() #show the graph in a new window
plt.clf() #close the graph