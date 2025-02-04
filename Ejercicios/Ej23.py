# Crear una lista de números que son múltiplos de 3 y 5.
# Crea una función que devuelva una lista de números múltiplos de 3 o 5 en un rango
# de 1 a N.

def multiplos(num):
    lista = []
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            lista.append(i)
    return lista

num = int(input("Escribe un número: "))
lista = multiplos(num)
print("Los números múltiplos de 3 y 5 entre 1 y", num, "son:", lista)