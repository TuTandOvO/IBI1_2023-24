import numpy as np
import matplotlib.pyplot as plt
# Use numpy and matplotlib.pyplot as tools
# Since I want to record the Susceptible, infected, recovered people each day during 1000 days, it is reasonable to use for statement 
# Infected possibility is 0.3*infected population rate, recover possibility is 0.05
# Lists are needed to recored each day change
# When a new number of population is formed, the data can append into the list
infect = 1
N = 10000
recover = 0
Susceptible = N - infect

# set initial lists
array_recover = [recover]
array_infect = [infect]
array_susceptible = [Susceptible]

for i in range(1, 1000):  # Loop from 1 to 1000 (to match number of iterations)
    p1 = 0.3 * infect / N
    p2 = 0.05
    infect_random = np.random.choice(range(2),array_susceptible[i-1],p=[p1,1-p1])
    infect_new = np.sum(infect_random==0)
    recover_random = np.random.choice(range(2),array_infect[i-1],p=[p2,1-p2])
    recover_new = np.sum(recover_random==0)
    infect = infect + infect_new - recover_new
    recover = recover + recover_new
    Susceptible = N-infect-recover
    array_infect.append(infect)  # Append daily infections
    array_recover.append(recover)  # Append recoveries
    array_susceptible.append(Susceptible)

# Plotting the results
plt.plot(range(0, 1000), array_susceptible, label='Susceptible')
plt.plot(range(0, 1000), array_infect, label='Infected')  # Plot cumulative infections
plt.plot(range(0, 1000), array_recover, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model Simulation')
plt.legend() # show the legends
plt.show()
plt.clf()


