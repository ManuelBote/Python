# Verificar si una cadena es un palíndromo.
# Crea una función que verifique si una cadena de texto es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)

def palindromo(cadena):
    if cadena == cadena[::-1]:
        return True
    else:
        return False
    
cadena = input("Escribe una cadena: ")

if palindromo(cadena):
    print("La cadena", cadena, "es un palíndromo")
else:
    print("La cadena", cadena, "no es un palíndromo")