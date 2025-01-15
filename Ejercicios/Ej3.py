# Encontrar el número más grande en una lista. Implementa una función que encuentre y devuelva el número mayor en una lista de enteros.

def mayor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

lista = []
while True:
    #La lista se cerrara al ingresar un numero negativo
    num = int(input("Introduce un numero a la lista: "))
    if num < 0:
        break
    else:
        lista.append(num)
        
print("El numero mayor de la lista es:",mayor(lista)) 
