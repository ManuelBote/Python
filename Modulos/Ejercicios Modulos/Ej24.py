# Crea un array de 1 dimensión que contenga los 40 primeros números pares.
# Seguidamente aplica un filtro al array anterior de modo que obtengas un
# array formado por los números mayores de 20 pertenecientes al array
# anterior. El filtro se debe de construir rellenando un array booleano mediante
# estructuras condicionales e iteradores.

import numpy as np

num = np.arange(0, 40, 2)

filtro = (num > 20)
array2 = num[filtro]
print(array2) 



