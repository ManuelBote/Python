# Imprimir los divisores de un número.
# Escribe una función que imprima todos los divisores de un número dado.

def divisores(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end = ' ')


num = int(input("Escribe un numero: "))
divisores(num)