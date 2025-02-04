# Contar las palabras de una cadena de texto.
# Escribe una función que cuente cuántas palabras contiene una cadena de texto.

def palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

cadena = input("Escribe la cadena de texto: ")
palabras = palabras(cadena)
print("La cadena de texto tiene", palabras, "palabras")
