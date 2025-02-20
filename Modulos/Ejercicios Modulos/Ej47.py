#  Crea un array que contenga el grupo sanguíneo de 20 personas (fruto de otra
# encuesta). Al preguntar a otras 20 personas más, se ha obtenido otro array
# de 20 elementos. Elabora, a partir de los dos arrays anteriores, un conjunto
# formado por los grupos sanguíneos que han aparecido en ambas encuestas.
# Finalmente, muestra el conjunto por pantalla.

import numpy as np

import numpy as np

# Array con los grupos sanguíneos de las primeras 20 personas
sangre1 = np.array(['O+', 'A-', 'B+', 'AB+', 'O-', 'A+', 'B-', 'O+', 'AB-', 'A+',
                                        'B+', 'O-', 'A-', 'O+', 'AB+', 'B-', 'A+', 'O+', 'A-', 'B+'])

# Array con los grupos sanguíneos de las siguientes 20 personas
sangre2 = np.array(['A+', 'O+', 'O-', 'AB+', 'A-', 'B+', 'AB-', 'O+', 'B-', 'O+',
                                        'A-', 'AB+', 'B+', 'A+', 'O-', 'B-', 'A+', 'AB-', 'O+', 'O-'])

# Obtener los grupos sanguíneos comunes en ambas encuestas
grupos = np.intersect1d(sangre1, sangre2)

print(grupos)