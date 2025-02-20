#  Crea un array que contenga el lugar de nacimiento de 20 personas (fruto de
# una última encuesta). Al preguntar a otras 20 personas más, se ha obtenido
# otro array de 20 elementos. Elabora, a partir de los dos arrays anteriores, un
# conjunto formado por las localidades de la primera encuesta que no están
# presentes en la segunda y las de la segunda que no están presentes en la
# primera

import numpy as np

sitios1 = np.array(['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao', 'Malaga', 'Zaragoza', 'Alicante', 'Granada', 'Oviedo',
                              'Santander', 'Córdoba', 'Badajoz', 'Murcia', 'La Coruña', 'Salamanca', 'Valladolid', 'Pamplona', 'Logroño', 'Huesca'])

sitios2 = np.array(['Madrid', 'Valencia', 'Alicante', 'Sevilla', 'Zaragoza', 'Granada', 'Murcia', 'Oviedo', 'Córdoba', 'Badajoz',
                              'Bilbao', 'Huesca', 'Salamanca', 'La Coruña', 'Santiago', 'Gijón', 'Pamplona', 'Logroño', 'Valladolid', 'San Sebastián'])

diferentes = np.setxor1d(sitios1, sitios2)
diferentes2 = np.setxor1d(sitios2, sitios1)

print(diferentes)
print(diferentes2)
