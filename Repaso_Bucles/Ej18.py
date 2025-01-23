# Dada una lista, escribe un programa que recorra la lista y cree un diccionario donde las claves sean 
# los índices de la lista y los valores sean los elementos de la lista.

def diccionario(lista):
    diccionario = {}
    for i in range(len(lista)):
        diccionario[i] = lista[i]
    return diccionario

lista = [2, 1, 20, 31, 4]

print(diccionario(lista))