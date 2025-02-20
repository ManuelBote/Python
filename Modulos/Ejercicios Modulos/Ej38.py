#  Establece el código y las sentencias adecuadas para calcular
# simultáneamente la función matemática factorial de 2 números n y m a partir
# de dos arrays de n y m elementos. Después de realizar las operaciones,
# muestra el resultado de ambas funciones en un mismo array.

import numpy as np

n = 5
m = 6

array1 = np.arange(1, n + 1)
array2 = np.arange(1, m + 1)

factorial1 = np.prod(array1)
factorial2 = np.prod(array2)

resultado = np.array([factorial1, factorial2])

print(resultado)