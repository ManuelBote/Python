# Crea un array de 2 dimensiones que contenga los 10 primeros números
# impares. Seguidamente, itera y muestra los elementos de los subarrays del
# array anterior empleando otra función diferente al for…in. Muestra también
# los 2 primeros números de cada uno de los subarrays y finalmente, muestra
# todos los elementos enumerados por filas y columnas

import numpy as np

impares = np.array([[1,3,5,7,9],[11,13,15,17,19]])

def funcion(x):
    for i in x:
        print(i, end=" ")
    print()

funcion(impares)

print("==============================================")

def funcion2(x):
    for i in x:
        cont = 1
        for j in i:
            if cont <= 2:
                print(j, end=" ")
            cont += 1
        print()

funcion2(impares)

print("==============================================")

def funcion3(x):
    cont = 1
    for i in x:
        cont2 = 1
        print("Fila",cont,": ", end="")
        for j in i:
            print("Columna",cont2,": ", j,"    ", end=" ")
            cont2 += 1
        print()
        cont += 1

funcion3(impares)
