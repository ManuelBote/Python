#  Recibe una lista de números y muestra la suma total de todos los elementos
# de la lista.

lista = []

while True:
    numero = int(input("Ingrese un número o -1 para terminar: "))
    if numero == -1:
        break
    else:
        lista.append(numero)

suma = sum(lista)
print("La suma de los elementos de la lista es:", suma)