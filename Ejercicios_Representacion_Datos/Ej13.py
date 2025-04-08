# Crea un array que contenga el número de sobresalientes, notables,
# suficientes y suspensos en el módulo de Programación de Inteligencia
# Artificial del Curso de Especialización en Inteligencia Artificial y Big Data.
# Seguidamente, representa los datos anteriores en un gráfico circular para
# observar la proporción de cada nota en relación a la totalidad de la clase.
# Además, establece leyendas en cada porción para poder diferenciar qué
# porcentaje está asociado a cada una de ellas

import matplotlib.pyplot as plt
import numpy as np

notas = [4, 7, 8, 3]
categorias = ['Sobresaliente', 'Notable', 'Suficiente', 'Suspenso']

plt.figure(figsize=(10, 10))
plt.pie(notas, labels=categorias, autopct='%1.1f%%', startangle=90)
plt.title('Notas de la Clase')

plt.show()
