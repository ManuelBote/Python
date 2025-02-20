# Establece el código y las sentencias adecuadas para comprobar, mediante la
# visualización de un array por pantalla, si el 10 es múltiplo de los 10 primeros
# números naturales (1,2…,10).

import numpy as np

numeros = np.arange(1, 11)

for i in range(10):
    if numeros[i] % 10 == 0:
        print(numeros[i], "es múltiplo de 10")
    else:
        print(numeros[i], "no es múltiplo de 10")

        