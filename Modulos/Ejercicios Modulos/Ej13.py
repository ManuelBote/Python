# Crea una array de 1 dimensión que contenga los 5 primeros números pares.
# Seguidamente, itera y muestra los elementos del array anterior. Crea un array
# de 2 dimensiones con los 10 primeros números pares. A continuación itera y
# muestra cada uno de los subarrays del array anterior. Por último, crea un
# array de 3 dimensiones que contenga los 20 primeros números pares para
# después iterar y mostrar cada uno de los elementos de los subarrays de
# menor tamaño.

import numpy as np

pares = np.array([2,4,6,8,10])

for i in pares:
    print(i, end=" ")
print()

print("==============================================")

num = np.array([[2,4,6,8,10],[12,14,16,18,20]])

for i in num:
    for j in i:
        print(j, end=" ")
    print()


print("==============================================")


num2 = np.array([[[2,4,6,8,10],[12,14,16,18,20]],[[22,24,26,28,30],[32,34,36,38,40]]])

for i in num2:
    for j in i:
        cont = 1
        for k in j:
            if cont == 1:
                print(k, end=" ")
            cont += 1
        print()