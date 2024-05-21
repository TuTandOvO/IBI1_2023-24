import matplotlib.pyplot as plt
import numpy as np
# Import matplotlib.colors as colors
# The infected has 0.3 possibility to infect neighboring people
N = 100  
gamma = 0.05
beta = 0.3
plt.figure ( figsize =(6 ,4) , dpi=150)
population = np.zeros ( (N , N) )# create a 100x100 matrix, each dot represent one person
outbreak = np.random.choice (range(100) ,2)
population [ outbreak[0] ,outbreak [1]] = 1
for t in range(100):
    # Infection start
    for i in range(N):
        for j in range(N):
            if population[i,j] == 1: # if the number is 1, it means that this person is infected
                for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1)]:
                    if 0 <= x < N and 0 <= y < N: # confirm x,y are in the matrix
                        if np.random.random() < beta: # if the random number is smaller than beta, it means this person will infect a neighbor
                            population[x,y] = 1
    # Recover
    for i in range(N):
        for j in range(N):
            if population[i,j] == 1:
                if np.random.random() < gamma: # if the random number is smaller than gamma, it means this person will recover
                    population[i,j] = 2
    plt.clf() # clear the figure
    plt.imshow ( population , cmap='viridis' , interpolation='bilinear' )
    plt.title('SIR Model '+str(t)+' days')
    plt.pause(0.1) # pause for 0.1 seconds
plt.pause(10)
plt.clf()
