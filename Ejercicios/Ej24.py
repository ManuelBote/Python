# Imprimir las primeras N filas de Pascal.
# Crea una función que imprima las primeras N filas del Triángulo de Pascal.

def triangulo(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

num = int(input("Escribe el número de filas: "))
triangulo(num)