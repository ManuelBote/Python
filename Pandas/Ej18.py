# Representa gráficamente el peso, la altura, el IMC, el IGC y el grupo
# sanguíneo frente a las 50 personas pertenecientes a un barrio determinado.

import pandas as pd
import matplotlib.pyplot as plt

# Usamos el archivo del ejercicio 12 para realizar la lectura de datos
archivo = pd.read_json("Python\Pandas\Ej12.json")
dataframe = pd.DataFrame(archivo)

dataframe.plot()
plt.show()