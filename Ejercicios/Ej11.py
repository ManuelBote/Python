# Generar la secuencia de Fibonacci hasta N. Crea una función que genere los primeros N números de la secuencia Fibonacci.

fibonnacci = [0,1]

def calculo(num):
    a,b = 0,1
    while b < num:
        sum = a + b
        a = b
        b = sum
        if b < num:
            fibonnacci.append(sum)
    return fibonnacci


num = int(input("Ingrese un número: "))
print(calculo(num))