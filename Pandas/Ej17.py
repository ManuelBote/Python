# Representa gráficamente las faltas de asistencia de los alumnos, alumnas,
# profesores y profesoras de un centro educativo frente a los 31 días del mes
# de enero.

import pandas as pd
import matplotlib.pyplot as plt

# Usamos el archivo del ejercicio 11 para realizar la lectura de datos
archivo = pd.read_json("Python\Pandas\Ej11.json")
dataframe = pd.DataFrame(archivo["enero"])

dataframe.plot()
plt.show()