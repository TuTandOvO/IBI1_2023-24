import matplotlib.pyplot as plt
import numpy as np
# import matplotlib.colors as colors
N = 100  
gamma = 0.05
beta = 0.3
plt.figure ( figsize =(6 ,4) , dpi=150)
population = np.zeros ( (N , N) )# create a 100x100 matrix
# population [4 ,12] #check what number is in row 4, column 12
outbreak = np.random.choice (range(100) ,2)
population [ outbreak[0] ,outbreak [1]] = 1
for t in range(100):
    # Infection start
    for i in range(N):
        for j in range(N):
            if population[i,j] == 1:
                for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1)]:
                    if 0 <= x < N and 0 <= y < N:
                        if np.random.random() < beta:
                            population[x,y] = 1
    # Recover
    for i in range(N):
        for j in range(N):
            if population[i,j] == 1:
                if np.random.random() < gamma:
                    population[i,j] = 2
    plt.clf()
    plt.imshow ( population , cmap='viridis' , interpolation='bilinear' )
    plt.title('SIR Model '+str(t)+' days')
    plt.pause(0.1)
plt.pause(10)
plt.clf()
