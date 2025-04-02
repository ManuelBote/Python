# Pide al usuario ingresar una lista de números y muestra el número más
# grande de la lista.


lista = []

while True:
    numero = int(input("Ingrese un número o -1 para terminar: "))
    if numero == -1:
        break
    else:
        lista.append(numero)

numero = max(lista)
print("El número más grande de la lista es:", numero)