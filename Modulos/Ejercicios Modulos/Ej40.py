# Crea un array que contenga el precio de un producto determinado en cada
# uno de los meses de 2024. A partir del array anterior, crea un array que
# contenga la variación de la diferencia del valor del precio del producto
# mencionado a lo largo del año 2024.

import numpy as np

precio = np.array([12, 13, 12, 11, 14, 15, 16, 15, 15, 12, 14, 13])

variacion = np.diff(precio)

print(variacion)