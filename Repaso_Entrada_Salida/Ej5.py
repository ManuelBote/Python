# Crea un programa que reciba una lista de números y pida al usuario ingresar
# un número. Si el número está en la lista, imprímelo junto a su posición en la
# lista.

lista = []

while True:
    numero = int(input("Ingrese un número: "))
    if numero == -1:
        break
    else:
        lista.append(numero)

numero = int(input("Ingrese un número: "))

if numero in lista:
    print(numero, "está en la lista en la posición", lista.index(numero))
else:
    print(numero, "no está en la lista")    