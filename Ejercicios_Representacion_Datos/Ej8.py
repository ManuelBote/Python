# Crea un array que contenga la altura (en cm) de 20 personas y otro array que
# contenga el número de pie de dichas personas sometidas a una encuesta.
# Seguidamente, representa los datos anteriores en un gráfico de dispersión
# para comprobar si existe alguna correlación entre la altura de una persona y
# su número de calzado. Además, establece un mapa de colores y modifica el
# tamaño y opacidad de los puntos de dispersión
import matplotlib.pyplot as plt
import numpy as np 

altura_cm = np.array([160, 165, 170, 155, 180, 175, 172, 168, 169, 166,
                      178, 182, 185, 160, 163, 177, 171, 174, 176, 181])
numero_pie = np.array([37, 38, 41, 36, 44, 42, 41, 40, 40, 39,
                       43, 45, 46, 38, 37, 43, 41, 42, 43, 44])


plt.scatter(altura_cm, numero_pie, color='red',cmap='viridis', s=100, alpha=0.5)

plt.show()