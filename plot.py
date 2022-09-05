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

plt.figure(figsize=(10, 5.4), layout='constrained')
plt.plot(x, np.asarray(y[0]), label='2.1')
plt.plot(x, np.asarray(y[1]), label='1,91')
plt.plot(x, np.asarray(y[2]), label='1,53')
plt.plot(x, np.asarray(y[3]), label='1,09')
plt.plot(x, np.asarray(y[4]), label='0,685')
plt.plot(x, np.asarray(y[5]), label='0,28')
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()

