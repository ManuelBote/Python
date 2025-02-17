# Escribe un programa que calcule el precio de un artículo después de aplicar
# un descuento. Si el artículo cuesta más de 100, aplica un 10% de descuento;
# si cuesta 50 o más pero menos de 100, aplica un 5% de descuento; si es
# menor de 50, no hay descuento.

precio = float(input("Ingrese el precio del artículo: "))

if precio >= 100:
    precio = precio * 0.9
elif precio >= 50:
    precio = precio * 0.95

print("El precio después del descuento es:", precio)