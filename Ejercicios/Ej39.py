# Determinar si dos listas son anagramas entre sí.
# Escribe una función que verifique si dos listas contienen los mismos elementos en
# cualquier orden

def anagrama(lista1, lista2):
    if len(lista1) != len(lista2):
        return False
    else:
        for i in lista1:
            if i in lista2:
                lista2.remove(i)
        if len(lista2) == 0:
            return True
        else:
            return False

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 3, 5, 1, 2]
lista3 = [1, 2, 3, 4, 5, 6]

print(anagrama(lista1, lista2))
print(anagrama(lista1, lista3))
                
                
