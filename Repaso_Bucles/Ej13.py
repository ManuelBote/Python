# Dada una lista de cadenas de texto, escribe un programa que concatene todas las cadenas en una sola.


def frase(lista):
    frase = ""
    for i in lista:
        frase += i
        frase += " "
    return frase

lista = ["Hola", "Mundo", "Python", "Teclado"]

print(frase(lista))