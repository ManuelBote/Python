# Crea una serie mediante el paquete Pandas que contenga el número de pasos dados en los 20 primeros días de un mes. 
# Muestra la serie completa por pantalla y, después, los pasos dados en los días 8 y 13

import pandas as pd

pasos = [4000, 5000, 3000, 4000, 5000, 3000, 6000, 2000, 5000, 3000, 4000, 5000, 3000, 4000, 5000, 3000, 6000, 2000, 3000, 7000]

serie = pd.Series(pasos)

print(serie)

print(serie[[8,13]])