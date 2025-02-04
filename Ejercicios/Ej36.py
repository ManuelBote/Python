# Detectar si una lista tiene elementos duplicados.
# Crea una función que determine si una lista contiene elementos duplicados.

import random

def duplicados(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

lista = []
for i in range (10):
    lista.append(random.randint(1, 20))
print(lista)

if duplicados(lista):
    print("La lista tiene elementos duplicados")
else:
    print("La lista no tiene elementos duplicados")
