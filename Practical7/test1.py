import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pwd = os.getcwd()
print(pwd)
ls = os.listdir()
print(list)
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")
first_5 = dalys_data.head(5)
print(first_5)
dalys_data.info()
a = dalys_data.describe()# provide basic infomation such as  this numbers of entries, mean, SD and a number of quantiles
print(a)
dalys_data.iloc[4,2]# point to the fifth row in the third column
dalys_data.iloc[2,0:5]# 0:5 means 0,1,2,3,4 and 5 will not be included
dalys_data.iloc[0:2,:]# choose the first and second rows and choose all the columns
dalys_data.iloc[0:10:2,0:5]# choose rows 0:10 with step length in 2
dalys_data.iloc[0:3,[0,1,3]]#choose 0:3 rows and columns only include the first, second and theforth
my_columns = [True, True, False, True] #use Bolleans to determine which also mean [0,1,3] 
dalys_data.iloc[0:3,my_columns]
dalys_data.loc[2:4,"Year"]# loc is different from iloc that 0:2 means 2,3,4 and it can search the title
# dalys_data.loc[blabla,"DALYs"] # blabla is not included in the table
dalys_data.loc[dalys_data['Entity']=='Afghanistan', 'DALYs'] #use judge statement that check if the Entity is Afghanistan which include Booleans
China_data = dalys_data.loc[dalys_data['Entity']=='China',['Year','DALYs']]# use[] to inform that these are all in rows or columns
type(dalys_data['Entity']=='China')#<class 'pandas.core.series.Series'>
list(dalys_data['Entity']=='China')#change it into list 
pd.DataFrame(list(dalys_data['Entity']=='China'))# change list into Dataframe which is included in pandas
plt.plot(China_data.Year, China_data.DALYs, 'b+')#b+ means blue cross and r+ means red cross, bo mwans blue dot
plt.xticks(China_data.Year, rotation=-90)#ratate the number on x-axis
plt.show()
plt.clf()