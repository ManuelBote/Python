# Crea un array que contenga el número de habitantes de una determinada
# población para cada uno de los meses de 2024. A partir del array anterior,
# elabora un nuevo array que contenga la diferencia de población entre un mes
# y el siguiente a lo largo de 2024

import numpy as np

poblacion = np.array([10000, 9000, 11000, 11500, 12300, 12500, 12000, 13500, 14600, 14500, 15000, 14700])

diferencia = np.diff(poblacion)

print(diferencia)