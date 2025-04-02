# Pide al usuario ingresar dos listas de números y luego crea una tercera lista
# que sea la concatenación de ambas listas.

lista1 = []
lista2 = []
lista3 = []

print("Lista 1")
while True:
    numero = int(input("Ingrese un número o -1 para terminar: "))
    if numero == -1:
        break
    else:
        lista1.append(numero)

print("Lista 2")
while True:
    numero = int(input("Ingrese un número o -1 para terminar: "))
    if numero == -1:
        break
    else:
        lista2.append(numero)


lista3 = lista1 + lista2
print("La concatenación de las listas es:", lista3)