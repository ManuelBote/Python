#  Representa gráficamente la temperatura media, temperatura máxima,
# temperatura mínima, probabilidad de precipitación y porcentaje de humedad
# frente a los días del mes de enero.

import pandas as pd
import matplotlib.pyplot as plt

# Usamos el archivo del ejercicio 7 para realizar la lectura de datos
dataframe = pd.read_csv("Python\Pandas\Ej7.csv")

dataframe.plot(x="Día")
plt.show()