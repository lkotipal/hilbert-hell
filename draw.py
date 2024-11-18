import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

x_prime, x, y, z, x_inv = np.genfromtxt('out', unpack=True)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(x, y, z, linewidth=1)
fig.savefig('figure.png', dpi=1200)
