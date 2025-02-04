# Generar una lista de números primos hasta N.
# Escribe una función que devuelva una lista de números primos hasta un número
# dado utilizando el método de la Criba de Eratóstenes

def primos(n):
    # Se añade el dos a la lista, por que el numero dos es un primo y con esta funcion no lo contamos
    primos = [2]
    i = 2
    while i <= n:
        if i > 2:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primos.append(i)
        i += 1
    return primos


n = int(input("Escribe un número: "))
primos = primos(n)
print("Los números primos hasta", n, "son:", primos)