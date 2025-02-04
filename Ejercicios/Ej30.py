# Imprimir el reverso de una lista.
# Implementa una función que reciba una lista y devuelva su reverso

import random

def reverso(lista):
    lista_reverso = lista[::-1]
    return lista_reverso

lista = []
for i in range (10):
    lista.append(random.randint(1, 100))
print(lista)
lista_reverso = reverso(lista)
print(lista_reverso)