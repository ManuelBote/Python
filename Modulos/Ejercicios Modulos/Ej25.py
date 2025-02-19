# Crea un array que contenga los ingresos obtenidos por un empleado en la
# primera quincena de todos los meses de 2024. Crea otro array que contenga
# los ingresos obtenidos por un empleado en la segunda quincena de todos los
# meses de 2024. Finalmente, suma los elementos de ambos arrays y elabora
# un array que contenga los ingresos totales del empleado durante 2024.

import numpy as np
quincena1 = np.array([560, 560, 580, 540, 540, 550, 570, 590, 600, 610, 620, 630])
quincena2 = np.array([550, 560, 560, 560, 540, 570, 520, 530, 540, 660, 550, 700])

total = quincena1 + quincena2
print(total)