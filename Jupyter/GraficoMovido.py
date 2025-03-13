import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection = '3d')

z = np.linspace(0, 15, 1000)
x = np.sin(z)
y = np.cos(z)

ax.plot3D(x, y, z, "green")

for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(0.001)

plt.show()