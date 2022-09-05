import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(0, 15, 6)
x = [
        [0, 0.3, 2.6, 4.1, 2.5, 1.2],
        [3, 3.8, 5.4, 5.5, 4, 2.7],
        [6, 6.4, 7.3, 7.5, 6.6, 5.7],
        [9, 8.6, 8.4, 8.4, 8.2, 8.4],
        [12, 11.1, 10.7, 10.8, 11, 11.7],
        [15, 14.4, 14.1, 14.1, 14.3, 14.9],
        ]
labels = ['2,100', '1,910', '1,530', '1,090', '0,685', '0,280']

plt.figure(figsize=(10, 5.4), layout='constrained')

for i in range(0, 6):
    plt.plot(np.asarray(x[i]), y, label=labels[i])

for i in range(1, 6):
    plt.fill_betweenx(y, x[i-1], x[i])

plt.fill_betweenx(y, 0, x[0])
plt.fill_betweenx(y, x[5], 15)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()
