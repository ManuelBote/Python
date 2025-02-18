# Representa en un gráfico la variación de ventas que experimenta una
# empresa a lo largo de un año. Establece los puntos del gráfico con forma
# cuadrada, tamaño relativamente grande, con un borde de color verde y con
# un color de relleno rosa (además de un color de línea negro).

import numpy as np
import matplotlib.pyplot as plt

meses = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
ventas = np.array([100, 120, 110, 130, 140, 150, 160, 170, 150, 190, 200, 210])

plt.plot(meses, ventas, color='black', marker='s', markersize=10, markeredgewidth=2, markeredgecolor='green', markerfacecolor='pink')

plt.show()