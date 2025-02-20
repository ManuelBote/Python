# Establece el código y las sentencias adecuadas para comprobar, mediante la
# visualización de un array por pantalla, las potencias de 20 a la unidad, al
# cuadrado, al cubo, a la cuarta y a la quinta

import numpy as np

potencias = np.power(20, np.arange(1, 6))
print(potencias)