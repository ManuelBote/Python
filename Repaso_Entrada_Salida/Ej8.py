# Pide al usuario ingresar una lista de números y elimina los elementos
# duplicados usando un diccionario para hacer un conteo y luego mostrando la
# lista sin repeticiones.

lista = []
diccionario = {}

while True:
    numero = int(input("Ingrese un número o -1 para terminar: "))
    if numero == -1:
        break
    else:
        lista.append(numero)


for i in lista:
    if i in diccionario:
        diccionario[i] += 1
    else:    
        diccionario[i] = 1

for i in lista:
    if diccionario[i] != 1:
        lista.remove(i)

print("La lista sin repeticiones es:", lista)  