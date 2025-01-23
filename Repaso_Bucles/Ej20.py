# Dada una lista de tuplas, escribe un programa que ordene la lista según el segundo elemento de cada tupla

def ordenar(lista):
    lista = sorted(lista, key=lambda x: x[1])
    return lista

lista = [(5, 9), (3, 1), (2, 2), (1, 6), (8, 4)]

print(ordenar(lista))
    
    