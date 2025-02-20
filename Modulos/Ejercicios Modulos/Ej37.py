# Establece el código y las sentencias adecuadas para calcular la función
# matemática factorial de un número n a partir de un array de n elementos.
# Después de realizar las operaciones, muestra el resultado por pantalla

import numpy as np

n = 5 

array = np.arange(1, n + 1)

factorial = np.prod(array)

print(factorial)
