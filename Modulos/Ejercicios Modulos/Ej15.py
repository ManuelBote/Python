# Crea dos arrays de 1 dimensión (el primero de ellos debe contener los 3
# primeros números primos y el segundo de ellos debe contener los 3
# siguientes). Seguidamente, une los dos arrays anteriores por fila y después
# por columnas. Crea un array de 2 dimensiones que contenga los 10 primeros
# números primos y, a continuación, une los subarrays de cada array
# bidimensional.


import numpy as np

array1 = np.array([2, 3, 5])
array2 = np.array([7, 11, 13])

print(np.vstack((array1, array2)))
print(np.hstack((array1.reshape(-1, 1), array2.reshape(-1, 1))))

print("==============================================")

array3 = np.array([[2,3,5,7,11], [13,17,19,23,29]])

print(np.concatenate(array3))
