# Escribe un programa que pida un nombre de usuario y una contraseña, y
# determine si los datos son correctos

usuario = input("Ingrese el nombre de usuario: ")
contraseña = input("Ingrese la contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("Acceso permitido")
else:
    print("Acceso denegado")    