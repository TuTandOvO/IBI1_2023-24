Average_day = {"Sleeping":8,"Classes":6,"Studying":3.5,"TV":2,"Music":1,"Other":3.5}
print(Average_day)
import numpy as py
import matplotlib.pyplot as plt
Hours_types = ["Sleeping","Classes","Studying","TV","Music","Other"]
Hours = [8,6,3.5,2,1,3.5]
plt.pie(Hours, labels = Hours_types)
plt.show()
plt.clf()