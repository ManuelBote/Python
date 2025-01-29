# Representa gráficamente el número de faltas de asistencia del alumnado en
# 5 asignaturas diferentes frente a los 50 primeros días del curso

import pandas as pd
import matplotlib.pyplot as plt

# Usamos el archivo del ejercicio 9 para realizar la lectura de datos
dataframe = pd.read_csv("Python\Pandas\Ej9.csv")

dataframe.plot(x="Día")
plt.show()