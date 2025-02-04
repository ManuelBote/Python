# Ordenar una lista de números de menor a mayor.
# Crea una función que ordene una lista de números en orden ascendente utilizando
# un algoritmo de ordenamiento sencillo (como burbuja)

import random

def ordenar(lista):
    lista2 = sorted(lista)
    return lista2

lista = []
for i in range (10):
    lista.append(random.randint(1, 100))
print(lista)

print(ordenar(lista))