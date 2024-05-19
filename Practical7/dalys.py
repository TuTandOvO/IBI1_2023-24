import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dalys_data = pd.read_csv(r"D:\IBI\IBI1_2023-24\Practical7\dalys-rate-from-all-causes(1).csv")

# Show the forth column from every 10th row, starting from the first row for the first 100 rows
specific_value = dalys_data.iloc[0:100:10,3]
print(specific_value)

# Use Booleans to check Afghanistan data
Afghanistan_data = dalys_data.loc[dalys_data['Entity']=='Afghanistan',:]

# Computed the mean DALY in China
CHINA_data = dalys_data.loc[dalys_data['Entity']=='China', ['DALYs']]
mean_value = np.mean(CHINA_data)
print('The mean DALYS value of China is',mean_value)
# The mean of DLAYs of China is 30677, but 2019 China DALYs is 22270 which is lower than the mean

# Plot showing the DALYs over time in China
DALYS_China = dalys_data.loc[dalys_data['Entity']=='China',['DALYs']]
Years_China = dalys_data.loc[dalys_data['Entity']=='China',['Year']]
plt.figure()
plt.plot(Years_China,DALYS_China)
plt.xlabel('YEAR')
plt.ylabel('DALYs')
plt.title('DALYs of China over time')

# Solutions for the question
High_data = dalys_data.loc[dalys_data['Entity']=='World Bank High Income',['Year','DALYs']]
Low_data = dalys_data.loc[dalys_data['Entity']=='World Bank Low Income',['Year','DALYs']]
x = High_data.Year
y = High_data.DALYs
a = Low_data.Year
b = Low_data.DALYs
plt.figure()
plt.xlabel('YEAR')
plt.ylabel('DALYs')
plt.title('DALYs comparasions between World Bank High Income and World Bank Low Income')
plt.plot(x,y,'b+',label= 'High Income')
plt.plot(a,b,'y--',label='Low Income')
plt.legend()
plt.show()
# The high income countries have less DALYs than the low income countries