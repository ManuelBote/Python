# Suma de números pares en un rango dado. Crea una función que sume los números pares en un rango de 1 a N (inclusive).

def suma (num):
    cont = 0
    for i in range(num+1):
        if (i%2) == 0:
            cont += i
    return cont


num = int(input("Indica un numero: "))
total = suma(num)

print("El total de la suma de los numeros pares anteriores a",num,"es igual a:",total)