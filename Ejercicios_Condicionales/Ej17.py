# Escribe un programa que simule un menú de opciones utilizando if-elif-else
# (como un switch). El usuario puede elegir entre varias opciones (Ejemplo: "1.
# Ver saldo", "2. Retirar dinero", "3. Salir") y el programa ejecuta una acción
# según la opción elegida.

print("Opción 1: Ver saldo")
print("Opción 2: Retirar dinero")
print("Opción 3: Salir")
print("===========================")

opcion = int(input("Ingrese la opción: "))

if opcion == 1:
    print("Su saldo es: 1000")
elif opcion == 2:
    print("Retirando dinero...")
elif opcion == 3:
    print("Saliendo...")
else:
    print("Opción incorrecta")