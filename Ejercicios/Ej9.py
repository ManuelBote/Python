# Imprimir números en orden descendente. Crea una función que imprima los números de un rango de N a 1 de manera descendente.7

def descendente(n):
    for i in range(n,0,-1):
        print(i)

num = int(input("Ingrese un número: "))
descendente(num)   

