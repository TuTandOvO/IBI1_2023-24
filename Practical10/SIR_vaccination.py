import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
infect = 1
N = 10000
recover = 0
vaccinated_rate = 0
for a in range(0,110,10):
    array_infect = [infect]
    Susceptible = N - infect - N*vaccinated_rate-recover
    for i in range(1, 1001):  # Loop from 1 to 1000 (to match number of iterations)
        p1 = 0.3 * infect / N
        p2 = 0.05
        infect_new = Susceptible * p1
        recover_new = infect * p2
        infect = infect + infect_new - recover_new
        recover = recover + recover_new
        Susceptible = N-infect-recover-N*vaccinated_rate
        array_infect.append(infect)  # Append daily infections
    plt.plot(range(0, 1001), array_infect, label=str(a)+'%')  # Plot cumulative infections
    # plt.plot(range(0, 1001), array_infect, label=a*0.1, color=cm. viridis (30)) which will change the graph into blue
    infect = 1
    recover = 0
    vaccinated_rate += 0.1
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model with different vaccination rates')
plt.legend() # show the legends
plt.show()
plt.clf()
plt.figure(figsize=(6,4),dpi=150)
plt.savefig('Herb_immunity.png',format='png') # In new matplotlib, type need to be changed to format
