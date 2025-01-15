# Crea un array mediante el módulo NumPy que contenga 5 números pares comprendidos entre el 40 y el 60. 
# Muestra el array por pantalla. Crea otro array de 3 dimensiones que contenga números mayores que 500 y muestra 
# por pantalla su dimensión. Crea un array de dimensión 8.

import numpy as np

array1 = np.array([42,44,46,48,50])
print(array1)

array2 = np.array([[510,520,530],[540,550,560],[570,580,590]])
print(array2.ndim)

array3 = np.array([1,2,3], ndmin=8 )
print(array3.ndim)