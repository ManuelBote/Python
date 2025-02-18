# Crea un texto y muéstralo por pantalla que contenga los siguientes tipos de
# constantes: prefijos (kilo, deca, etc.), prefijos binarios (kB, MB, GB, etc.),
# masas (gramos, libras, etc.), ángulos (grados, arcominutos, etc.), tiempos
# (segundos, minutos, etc.), longitudes (yardas, millas, etc.), presiones
# (atmósferas, bares, etc.), áreas (hectáreas, acres, etc.), volúmenes (litros,
# galones, etc.), velocidades (kilómetros hora, etc.), temperaturas (celsius,
# fahrenheit, etc.), energías (calorías, ergios, etc.), potencias (caballos de
# potencia, etc.) y fuerzas (kilogramos fuerza, libras fuerza, etc.). Para acceder
# a cada una de las constantes emplea el módulo SciPy.

import numpy as np
import scipy.constants as sc

print("El valor pi es:", np.pi)
print("En un kilobyte se almacenan:", sc.kibi, "bytes")