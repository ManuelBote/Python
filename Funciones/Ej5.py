#Realiza un programa principal que lea un dni y valide que es correcto(se debe comprobar tambien que tiene 9 caracteres)

def calcularLetra(num):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[num%23]

def validarDNI(dni):
    letra = dni[8]
    num = int(dni[:8])
    return letra.upper() == calcularLetra(num)
    


dni = input("Introduce un DNI: ")

while not validarDNI(dni) or len(dni) != 9:
    print("El DNI no es valido")
    dni = input("Introduce otro DNI: ")
    

print("El DNI es valido")
