# Dada una lista, escribe un programa que la invierta sin usar métodos adicionales de Python.

def invertir(lista):
    lista.reverse()
    return lista

lista = [20, 40, 15, 3, 10]

print(invertir(lista))