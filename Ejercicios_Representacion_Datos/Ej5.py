# Crea un array que contenga el número de hijos/as nacidos en una
# determinada población a lo largo de los meses de 2024 y otro array que
# contenga el número de hijos/as nacidos en otra población concreta a lo largo
# de los meses de 2024. Seguidamente, representa los datos anteriores en 2
# gráficos separados (o subgráficos), de forma que el primero se disponga
# encima del segundo.

import matplotlib.pyplot as plt
import numpy as np

array = np.array([20, 12, 11, 18, 24, 26, 20, 10, 15, 31, 19, 26])

array2 = np.array([34, 44, 32, 28, 31, 17, 26, 33, 38, 26, 43, 32])

plt.plot(array, label='Hijos/as nacidos en la población A', color='red')
plt.plot(array2, label='Hijos/as nacidos en la población B', color='green')

plt.show()  

