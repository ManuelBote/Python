# Crea un array que contenga el número de goles que ha marcado un equipo
# de fútbol en cada mes del año 2024. Seguidamente, representa los datos
# anteriores para observar las estadísticas goleadoras del equipo durante el
# pasado año. Además, establece etiquetas en los ejes,un título para el gráfico
# y estilos para ambos (alineamiento, familia de fuente, tamaño y color)

import matplotlib.pyplot as plt
import numpy as np

meses = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
goles = np.array([30, 16, 22, 5, 0, 1, 34, 19, 8, 21, 15, 7])

plt.plot(meses, goles, marker = 'o', color='red')
plt.xlabel("Mes")
plt.ylabel("Goles")
plt.title("Estadísticas Goleadoras")
plt.show()