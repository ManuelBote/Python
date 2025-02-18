# Crea dos arrays de 1 dimensión (el primero de ellos debe contener los 3
# primeros números elevados al cuadrado y el segundo de ellos debe contener
# los 3 siguientes elevados al cuadrado). Seguidamente, une los dos arrays por
# columnas para obtener un array bidimensional. Después une los arrays por
# fila y por columna (esto último de manera que se obtenga un array
# bidimensional donde los arrays anteriores sean los subarrays)

import numpy as np

array1 = np.array([1, 4, 9])
array2 = np.array([16, 25, 36])

array3 = np.hstack((array1.reshape(-1, 1), array2.reshape(-1, 1)))

print(np.vstack((array3, array3)))  
