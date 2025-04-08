# Crea un array que contenga el número de horas al día que invierten 20
# personas en ver la televisión y otro array que contenga las edades de dichas
# personas sometidas a una encuesta. Seguidamente, representa los datos
# anteriores en un gráfico de dispersión para comprobar si existe alguna
# correlación entre el número de horas dedicadas en ver TV y la edad del
# individuo.

import matplotlib.pyplot as plt
import numpy as np

array1 = np.array([7, 7, 8, 6, 8, 9, 2, 3, 4, 5, 6, 7, 1, 4, 3, 5, 6, 7, 3, 8])
array2 = np.array([62, 44, 54, 33, 26, 54, 20, 18, 7, 45, 66, 39, 40, 32, 35, 45, 56, 67, 34, 78])

plt.scatter(array1, array2, color='red')

plt.show()