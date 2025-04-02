# Pide al usuario ingresar varios valores que serán almacenados en una tupla.
# Luego, muestra la tupla invertida.

tupla = []

while True:
    valor = input("Ingrese un valor o -1 para terminar: ")
    if valor == "-1":
        break
    else:
        tupla.append(valor)

tupla.reverse()
print("La tupla invertida es:", tupla)