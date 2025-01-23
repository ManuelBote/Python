# Dada una lista de palabras, escribe un programa que cuente cuántas veces aparece cada palabra en la lista.

def contador(lista):
    cont = {}
    for i in lista:
        if i in cont:
            cont[i] += 1
        else:
            cont[i] = 1
    return cont

lista = ["a", "b", "c", "a", "c", "d", "b", "e", "a", "a", "c", "e"]

print(contador(lista))

cont = contador(lista)
for c, v in cont.items():
    print(c, v)