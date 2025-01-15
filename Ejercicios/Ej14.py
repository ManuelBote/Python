# Calcular el factorial de un número. Crea una función que calcule el factorial de un número de manera recursiva o iterativa.

def factorial(num):
    total = 1
    for i in range(1,num+1):
        total *= i
    return total
        

num = int(input("Ingrese un número: "))
print(factorial(num))

