# Pide al usuario un número e imprime el factorial de ese número utilizando una
# lista para guardar los valores intermedios.

numero = int(input("Ingrese un número: "))

factorial = 1
lista = [factorial]

for i in range(1, numero + 1):
    factorial *= i
    lista.append(factorial)

print("El factorial de",numero,"es",factorial)
print("La lista del factorial es:", lista)