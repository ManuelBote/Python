# Dada una lista, escribe un programa que cuente cuántas veces aparece un elemento específico.

def contador(lista, elemento):
    cont = 0
    for i in lista:
        if i == elemento:
            cont += 1
    return cont

lista = []
while True:
    lista.append(input("Introduce un elemento:"))
    w = input("Desea añadir otro elemento? (s/n)")
    if w == "n":
        break

elemento = input("Introduce el elemento que desea contar:")

print("El elemento", elemento, "aparece", contador(lista, elemento), "veces")