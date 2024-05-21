#we import somes tools in Python for making graphs
#In this session, since we want to change the time freely, so we need a variable to save values
#In the list, each string represents a variable
import numpy as py #inport python tools
import matplotlib.pyplot as plt #import python tools

#variables of the requested activity that can be modified
sleep = 8
classes = 6
study = 3.5
TV = 2
music = 1

#24-8-6-3.5-2-1=3.5
#so "other" occupies 3.5 hours on an average level
#another variable of the requested activity that can be modified
other = 24-sleep-classes-study-TV-music

#make a dictionary to record the data which can be changed by the variables
Average_day = {"Sleeping":sleep,"Classes":classes,"Studying":study,"TV":TV,"Music":music,"Other":other} #make a dictionary to record the data which can be changed by the variables
print(Average_day)
Hours_types = ["Sleeping","Classes","Studying","TV","Music","Other"] #make a list of types of hours spending
Hours = [sleep,classes,study,TV,music,other] #make a list of hours spending variables
plt.pie(Hours, labels = Hours_types,autopct='%1.1f%%') #use pie graph that is included in the matplotlib
plt.show() #show the graph in a new window
plt.clf() #close the graph

print('What is the average hours spending on each type of activities? Sleeping, Classes, Studying, TV, Music, Other')
user_input = input('Please input one type of activities: ')
if user_input in Average_day:
    print('The average hours spending on',user_input,'is',Average_day[user_input])
else:
    print('Sorry, the input is not correct')
