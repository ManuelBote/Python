#  Crea un array que contenga las edades de 20 personas aleatorias (fruto de
# una encuesta). A partir del array anterior, crea un conjunto de valores únicos
# con las edades de esas 20 personas (puesto que es bastante probable que la
# edad se repita entre los encuestados). Finalmente, visualiza el conjunto por
# pantalla.

import numpy as np

edades = np.random.randint(18, 80, 20)

conjunto = np.unique(edades)

print(edades)
print(conjunto)