# Crea un texto y muéstralo por pantalla que contenga los siguientes tipos de
# constantes: prefijos (kilo, deca, etc.), prefijos binarios (kB, MB, GB, etc.),
# masas (gramos, libras, etc.), ángulos (grados, arcominutos, etc.), tiempos
# (segundos, minutos, etc.), longitudes (yardas, millas, etc.), presiones
# (atmósferas, bares, etc.), áreas (hectáreas, acres, etc.), volúmenes (litros,
# galones, etc.), velocidades (kilómetros hora, etc.), temperaturas (celsius,
# fahrenheit, etc.), energías (calorías, ergios, etc.), potencias (caballos de
# potencia, etc.) y fuerzas (kilogramos fuerza, libras fuerza, etc.). Para acceder
# a cada una de las constantes emplea el módulo SciPy.

import scipy.constants as cs

texto = f"""
Prefijos:
- kilo: {cs.kilo} (1000)

Prefijos binarios:
- kB (kilobyte): {cs.kibi} bytes
- MB (megabyte): {cs.mebi} bytes
- GB (gigabyte): {cs.gibi} bytes

Masas:
- gramo: {cs.gram} gramos
- libra: {cs.lb} libras

Ángulos:
- grado: {cs.degree} grados
- arcominuto: {cs.arcminute} arcominutos

Tiempos:
- minuto: {cs.minute} minutos

Longitudes:
- yarda: {cs.yard} yardas
- milla: {cs.mile} millas

Presiones:
- atmósfera: {cs.atm} atmósferas
- bar: {cs.bar} bares

Áreas:
- hectárea: {cs.hectare} hectáreas
- acre: {cs.acre} acres

Volúmenes:
- litro: {cs.liter} litros
- galón: {cs.gallon} galones

Energías:
- caloría: {cs.calorie} calorías
- ergio: {cs.erg} ergios

Potencias:
- caballo de potencia: {cs.horsepower} caballos de potencia

Fuerzas:
- kilogramo fuerza: {cs.kgf} kilogramos fuerza
- libra fuerza: {cs.lbf} libras fuerza
"""

print(texto)