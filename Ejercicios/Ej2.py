# Contar cuántas veces aparece un número en una lista. Escribe una función que cuente la cantidad de veces que un número aparece en una lista dada.

def contador(num, lista):
    cont = 0
    for i in lista:
        if i == num:
            cont += 1
    return cont


lista = []
while True:
    #La lista se cerrara al ingresar un numero negativo
    num = int(input("Introduce un numero a la lista: "))
    if num < 0:
        break
    else:
        lista.append(num)

num = int(input("Introduce un numero a buscar en la lista: "))
cont = contador(num, lista)
print(lista)
print("El numero",num,"se encuentra",cont,"vez/veces en la lista")

    