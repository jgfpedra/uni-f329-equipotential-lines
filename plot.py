import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 15, 6)
y = [
        [0, 0.3, 2.6, 4.1, 2.5, 1.2],
        [3, 3.8, 5.4, 5.5, 4, 2.7],
        [6, 6.4, 7.3, 7.5, 6.6, 5.7],
        [9, 8.6, 8.4, 8.4, 8.2, 8.4],
        [12, 11.1, 10.7, 10.8, 11, 11.7],
        [15, 14.4, 14.1, 14.1, 14.3, 14.9],
        ]
labels = ['2,100', '1,910', '1,530', '1,090', '0,685', '0,280']

plt.figure(figsize=(10, 5.4), layout='constrained')
plt.plot(np.asarray(y[0]), x, label='2,100')
plt.plot(np.asarray(y[1]), x, label='1,910')
plt.plot(np.asarray(y[2]), x, label='1,530')
plt.plot(np.asarray(y[3]), x, label='1,090')
plt.plot(np.asarray(y[4]), x, label='0,685')
plt.plot(np.asarray(y[5]), x, label='0,280')
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()
plt.show()

