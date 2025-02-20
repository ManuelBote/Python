# Crea un array que contenga el sueldo de un empleado durante los 6 primeros
# meses de 2024. Crea otro array que contenga el sueldo de ese mismo
# empleado durante los últimos 6 meses de 2024. Finalmente, crea un array a
# partir de los anteriores que contenga el sueldo total ingresado en 2024 por el
# empleado.

import numpy as np

sueldo1 = np.array([10000, 10500, 11000, 11500, 12000, 12500])
sueldo2 = np.array([12000, 12500, 13000, 13500, 14000, 14500])

sueldo_total = np.concatenate((sueldo1, sueldo2))

print(sueldo_total)