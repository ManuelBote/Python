# Representa gráficamente la altura (en metros) que toma un balón golpeado
# hacia arriba en la Tierra y en 4 planetas más frente a los 50 primeros
# segundos de un minuto

import pandas as pd
import matplotlib.pyplot as plt

# Usamos el archivo del ejercicio 10 para realizar la lectura de datos
archivo = pd.read_json("Python\Pandas\Ej10.json")
dataframe = pd.DataFrame(archivo["alturas"])

dataframe.plot(y=["Tierra", "Marte", "Venus", "Jupiter", "Luna"])
plt.show()