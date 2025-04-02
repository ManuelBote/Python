# Crea un array que contenga el número de kilos que ha pesado el streamer
# Ibai Llanos durante todos los meses del año 2024. Seguidamente, representa
# los datos anteriores para observar el gran cambio físico que ha
# experimentado el susodicho. Además, establece una rejilla en el gráfico para
# poder visualizar mejor los valores de peso en cada mes.

import matplotlib.pyplot as plt
import numpy as np

peso = np.array([155, 150, 145, 140, 135, 130, 125, 120, 115, 110, 105, 100])
meses = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

plt.plot(meses, peso, linestyle = "-", color='red', linewidth=3)
plt.xlabel("Mes")
plt.ylabel("Peso (kg)")
plt.grid(True)
plt.show()