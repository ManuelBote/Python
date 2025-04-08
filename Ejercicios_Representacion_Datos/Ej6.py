# Crea cuatro arrays que contengan el número de horas de sueño de cuatro
# alumnos del IES Augustóbriga para cada día de la semana. Seguidamente,
# representa los datos anteriores en cuatro gráficos separados (de modo que
# los dos primeros gráficos se coloquen encima de los dos últimos) para poder
# observar mejor la calidad del sueño de los alumnos del centro. Además,
# establece un título individual para cada subgráfico y un título global para el
# conjunto completo

import matplotlib.pyplot as plt
import numpy as np

array1 = np.array( [7, 7, 8, 6, 8, 9, 10])
array2 = np.array( [5, 4, 5, 6, 7, 12, 11])
array3 = np.array( [8, 7, 7, 8, 8, 7, 8])
array4 = np.array( [5, 5, 4, 6, 3, 5, 6])

plt.plot(array1, label='Horas de sueño del IES Augustóbriga', color='red')
plt.plot(array2, label='Horas de sueño del IES Augustóbriga', color='green')
plt.plot(array3, label='Horas de sueño del IES Augustóbriga', color='blue')
plt.plot(array4, label='Horas de sueño del IES Augustóbriga', color='yellow')

plt.title('Horas de sueño de los alumnos del IES Augustóbriga')
plt.legend()

plt.show()
