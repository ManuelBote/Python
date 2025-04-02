# Pide al usuario ingresar varios productos con sus precios en un diccionario.
# Luego, muestra todos los productos junto con su precio.

diccionario = {}

while True:
    producto = input("Ingrese un producto: ")
    if producto == "-1":
        break
    precio = float(input("Ingrese el precio: "))
    diccionario[producto] = precio

for i in diccionario:
    print(i, ":", diccionario[i])