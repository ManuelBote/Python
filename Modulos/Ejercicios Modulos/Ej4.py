# Crea un array que contenga los 5 primeros números pares y muestra por pantalla la resta del cuarto elemento menos el segundo elemento. 
# Crea un array de dimensión 2 que contenga los 10 primeros números pares y muestra por pantalla el tercer elemento de la primera fila.
# Crea otro array de 3 dimensiones que contenga los 20 primeros números pares y muestra por pantalla el producto del primer número par por el último número par.

import numpy as np

array1 = np.array([2,4,6,8,10])
array2 = np.array([[2,4,6,8,10],[12,14,16,18,20]])
array3 = np.array([[[2,4,6,8,10],[12,14,16,18,20]],[[22,24,26,28,30],[32,34,36,38,40]]])
print("La resta del cuarto menos el segundos es:", array1[3]-array1[1])
print("El tercer elemento de la primera fila es:", array2[0,1])
print("El producto del primer numero par por el utlimo es:", array3[0,0,0]*array3[1,1,4])