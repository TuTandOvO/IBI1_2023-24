# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import cm
# infect = 1
# N = 10000
# recover = 0
# vaccinated_rate = 0
# array_infect = [infect]
# Susceptible = int(N - infect - N*vaccinated_rate-recover)
# Vaccinated_N = int(N - N*vaccinated_rate)
# array_susceptible = [Susceptible]

# for a in range(0,110,10):
#     for i in range(1, 1000):  # Loop from 1 to 1000 (to match number of iterations)
#         p1 = 0.3 * infect / N
#         p2 = 0.05
#         infect_random = np.random.choice(range(2),array_susceptible[i-1],p=[p1,1-p1])
#         infect_new = np.sum(infect_random==0)
#         recover_random = np.random.choice(range(2),array_infect[i-1],p=[p2,1-p2])
#         recover_new = np.sum(recover_random==0)
#         infect = infect + infect_new - recover_new
#         print(infect)
#         recover = recover + recover_new
#         Susceptible = Vaccinated_N-infect-recover
#         array_infect.append(infect)  # Append daily infections
#         array_susceptible.append(Susceptible)
    
#     plt.plot(range(0, 1000), array_infect, label=str(a)+'%')  # Plot cumulative infections
#     # plt.plot(range(0, 1000), array_infect, label=a*0.1, color=cm. viridis (30)) which will change the graph into blue
#     infect = 1
#     recover = 0
#     vaccinated_rate += 0.1
#     Susceptible = int(N - infect - N*vaccinated_rate-recover)
#     Vaccinated_N = int(N - N*vaccinated_rate)
# plt.xlabel('Time')
# plt.ylabel('Number of People')
# plt.title('SIR Model with different vaccination rates')
# plt.legend() # show the legends
# plt.show()
# plt.clf()
# plt.figure(figsize=(6,4),dpi=150)
# plt.savefig('Herb_immunity.png',format='png') # In new matplotlib, type need to be changed to format


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

infect = 1
N = 10000
recover = 0
vaccinated_rate = 0
array_infect = [infect]
Susceptible = int(N - infect - N * vaccinated_rate - recover)
Vaccinated_N = int(N - N * vaccinated_rate)
array_susceptible = [Susceptible]

for a in range(0, 110, 10):
    array_infect = [infect]
    array_susceptible = [Susceptible]
    for i in range(1, 1000):
        p1 = 0.3 * infect / N
        p2 = 0.05
        infect_random = np.random.choice(range(2), array_susceptible[i-1], p=[p1, 1-p1])
        infect_new = max(0, np.sum(infect_random == 0))
        recover_random = np.random.choice(range(2), array_infect[i-1], p=[p2, 1-p2])
        recover_new = max(0, np.sum(recover_random == 0))
        infect = max(0, infect + infect_new - recover_new)
        recover = max(0, recover + recover_new)
        Susceptible = max(0, Vaccinated_N - infect - recover)
        array_infect.append(infect)
        array_susceptible.append(Susceptible)

    plt.plot(range(0, 1000), array_infect, label=str(a)+'%')

    infect = 1
    recover = 0
    vaccinated_rate += 0.1
    Susceptible = int(N - infect - N * vaccinated_rate - recover)
    Vaccinated_N = int(N - N * vaccinated_rate)

plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model with different vaccination rates')
plt.legend()
plt.show()

plt.figure(figsize=(6, 4), dpi=150)
plt.savefig('Herb_immunity.png', format='png')
plt.clf()