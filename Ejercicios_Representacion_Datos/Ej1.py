# Crea un array que contenga el número de días lluviosos para cada mes del
# año 2024. Seguidamente, representa los datos anteriores para observar la
# variación de precipitaciones durante el pasado año. Además, establece
# etiquetas en los ejes vertical y horizontal.

import matplotlib.pyplot as plt
import numpy as np

lluviosos = np.array([13, 15, 20, 24, 12, 6, 0, 2, 4, 17, 20, 15])
meses = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

plt.plot(meses, lluviosos)
plt.xlabel("Mes")
plt.ylabel("Días lluviosos")
plt.show()

