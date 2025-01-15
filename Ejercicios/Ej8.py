# Contar las vocales en una cadena de texto. Escribe una función que cuente cuántas vocales (mayúsculas y minúsculas) hay en una cadena de texto.

vocales = ['a','e','i','o','u','A','E','I','O','U', "á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú"]

def contar(cadena):
    cont = 0
    for i in cadena:
        if i in vocales:
            cont += 1
    return cont

cadena = input("Introduce una cadena de texto: ")
cont = contar(cadena)
print("La cadena:",cadena,". Contiene",cont,"vocales") 