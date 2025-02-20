#  Crea un array que contenga los ingresos totales que recibe una cierta
# empresa en cada mes de 2024. Crea otro array que contenga el número de
# socios que integran esa misma empresa en cada mes de 2024. Finalmente,
# divide los elementos de ambos arrays y elabora un array que contenga los
# ingresos obtenidos por cada socio de la empresa durante 2024

import numpy as np

ingresos = np.array([10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500])
socios = np.array([5, 5, 6, 5, 7, 6, 7, 8, 9, 10, 10, 12])

ingresos_por_socio = ingresos / socios

print(ingresos_por_socio)