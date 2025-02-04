#  Verificar si una lista está ordenada de forma ascendente.
# Crea una función que determine si una lista de números está ordenada de manera
# ascendente

def ordenada(lista):
    list = sorted(lista, reverse=True)
    if lista == list:
        return print("La lista", lista,"está ordenada de forma ascendente")
    else:
        return print("La lista", lista, "no está ordenada de forma ascendente")
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

ordenada(lista)
ordenada(lista2)