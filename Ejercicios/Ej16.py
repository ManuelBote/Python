# Imprimir los números de Fibonacci menores que N.
# Escribe una función que imprima todos los números de Fibonacci menores que un número dado.

def menores (num): 
    n1, n2 = 0, 1
    while n1 < num:
        print(n1, end = ' ')
        n1, n2 = n2, n1 + n2
    

num = int(input("Escribe un numero: "))

menores(num)