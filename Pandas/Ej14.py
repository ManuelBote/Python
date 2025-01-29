# Representa gráficamente el número de habitantes correspondiente a 5
# poblaciones distintas frente a los 50 primeros años del siglo XX.

import pandas as pd
import matplotlib.pyplot as plt

# Usamos el archivo del ejercicio 8 para realizar la lectura de datos
dataframe = pd.read_csv("Python\Pandas\Ej8.csv")

dataframe.plot(x="Año")
plt.show()
