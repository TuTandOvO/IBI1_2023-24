import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")
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
plt.clf()