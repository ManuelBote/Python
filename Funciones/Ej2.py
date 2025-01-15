# Crea una funcion que retire un nombre de ususario y una contraseña y te devuelve verdadero si el nombre de usuario es "usuario1"
# Y la contraseña es "asd". Ademas se recibe el numero de intentos que se intenta hacer login. Solamente tenemos 3 oportunidades

def login(usuario, contraseña):
    if usuario == "usuario1" and contraseña == "asd":
        return True
    else:
        return False
    
cont = 1

while True:
    
    user = input("Introduce el numero de usuario: ")
    psw = input("Introduce la contraseña: ")
    if login(user,psw):
        print("Inicio de sesion correcto")
        print("Numero de intentos:", cont)
        break
    else:
        print("Usuario o contraseña incorrecto")
        cont+=1

    if cont == 4:
        print("Se terminaron los intentos")
        break