# Dada una lista de números, escribe un programa que filtre todos los números mayores a un valor específico

def mayor(lista, num):
    lista2 = []
    for i in lista:
        if i > num:
            lista2.append(i)
    return lista2

lista = [2, 1, 20, 31, 4, 11, 15, 22, 3, 10, 5, 6]
num = 10

print("Los numeros mayores a", num, "son:", mayor(lista, num))