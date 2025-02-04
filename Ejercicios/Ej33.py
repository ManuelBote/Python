# Crear un programa que imprima la serie de números de un triángulo de Pascal hasta N filas.
# Crea una función que imprima los números en el triángulo de Pascal para N filas.

def tri(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


n = int(input("Escribe un número: "))
tri(n)
