#  Crea un array que contenga el número de clases de una asignatura en cada
# mes de 2024. Crea otro array que contenga el número de faltas de asistencia
# de un alumno en esa misma asignatura en cada mes de 2024. Finalmente,
# resta los elementos de ambos arrays y elabora un array que contenga el
# número de días que ha asistido el alumno a la asignatura durante 2024

import numpy as np
clases = np.array([12, 10, 13, 14, 15, 12, 9, 11, 10, 9, 8, 7])
faltas = np.array([4, 3, 1, 2, 3, 0, 0, 1, 2, 3, 4, 5])

resta = clases - faltas
print(resta)