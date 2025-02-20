# Crea un array que contenga el precio que toma un cierto producto a lo largo
# de los meses de 2024. Crea otro array que contenga el descuento que toma
# ese mismo producto a lo largo de los meses de 2024. Finalmente, multiplica
# los elementos de ambos arrays para obtener el precio final con el descuento
# incorporado del producto durante 2024.

import numpy as np

precio = np.array([10, 11, 12, 11, 13, 10, 11, 14, 15, 15, 13, 14])
descuento = np.array([0, 5, 5, 10, 0, 5, 10, 15, 20, 0, 15, 10])

precio_con_descuento = precio - (precio * descuento / 100)

print(precio_con_descuento)

