# Pide al usuario ingresar un número y verifica si está en una tupla predefinida
# de números. Si es así, imprime su posición

numero = int(input("Ingrese un número: "))

lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

if numero in lista:
    print(numero, "está en la lista en la posición", lista.index(numero))
else:
    print(numero, "no está en la lista")