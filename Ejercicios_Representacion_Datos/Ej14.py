# Crea un array que contenga el género de cine favorito de 40 personas
# encuestadas en plena calle. Seguidamente, representa los datos anteriores
# en un gráfico circular para observar la proporción de cada respuesta dentro
# del cómputo global de la encuesta. Además, establece sombreado en el
# gráfico, una leyenda para ilustrar cada porción y resalta el sector más
# frecuente del gráfico.
import matplotlib.pyplot as plt
import numpy as np

cantidad = np.array([9, 12, 10, 6, 8, 7])
array = np.array(['Acción', 'Comedia', 'Drama', 'Terror', 'Ciencia Ficción', 'Romance'])

plt.figure(figsize=(10, 10))
plt.pie(cantidad, labels=array, autopct='%1.1f%%', startangle=90)
plt.title('Género de cine favorito')
plt.show()