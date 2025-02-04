# Encontrar el número de veces que un carácter aparece en una cadena.
# Crea una función que reciba una cadena y un carácter, y devuelva cuántas veces
# aparece ese carácter en la cadena.

def aparece(cadena, caracter):
    cont = 0
    for i in cadena:
        if i == caracter:
            cont += 1
    return cont

cadena = input("Escribe la cadena: ")
caracter = input("Escribe el carácter: ")
cont = aparece(cadena, caracter)        
print("El carácter", caracter, "aparece", cont, "veces en la cadena")