# Crear un programa que imprima una pirámide de asteriscos. Crea una función que reciba un número y devuelva una pirámide de asteriscos de ese tamaño.

def piramide(num):
    for i in range(1, num + 1):
        espacios = ' ' * (num - i)
        asteriscos = '*' * (2 * i - 1) 
        print(espacios + asteriscos)

num = int(input("Ingrese un número: "))
piramide(num)