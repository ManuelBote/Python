# Recibe una lista de números y crea una nueva lista con el doble de cada
# número, luego imprímela

lista = []
listaDoble = []

while True:
    numero = int(input("Ingrese un número o -1 para terminar: "))
    if numero == -1:
        break
    else:
        lista.append(numero)
        listaDoble.append(numero * 2)

for i in lista:
    print(i, ", el doble es:", listaDoble[lista.index(i)])