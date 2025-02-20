#  Calcula la hipotenusa de un triángulo rectángulo cuyo cateto base es igual a
# 7 y su cateto perpendicular es igual a 5. Finalmente, muestra el resultado por
# pantalla.

import numpy as np

base = 7
perpendicular = 5

hipotenusa = np.sqrt(base ** 2 + perpendicular ** 2)

print(hipotenusa)