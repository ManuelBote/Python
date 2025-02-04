# Calcular la suma de los números primos hasta N.
# Implementa una función que calcule la suma de los números primos en un rango
# hasta un número dado.

def es_primo(num2):
    for i in range(2, num2):
        if num2 % i == 0:
            return False
    return True

def primos(num):
    primos = 0
    for i in range(2, num + 1):
        if es_primo(i):
            primos += i
    return primos

num = int(input("Escribe un numero: "))
primos = primos(num)
print("Los números primos hasta", num, "son:", primos)
