# Imprimir todos los números primos en un rango dado.
# Crea una función que imprima todos los números primos en un rango de 1 a N.

def es_primo(num2):
    for i in range(2, num2):
        if num2 % i == 0:
            return False
    return True

def primos(num):
    primos = []
    for i in range(2, num + 1):
        if es_primo(i):
            primos.append(i)
    return primos

num = int(input("Escribe un numero: "))
primos = primos(num)
print("Los números primos hasta", num, "son:", primos)
