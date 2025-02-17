# Escribe un programa que calcule el impuesto que debe pagar una persona
# según su salario. Si el salario es menor a 20,000, el impuesto es del 5%, si
# está entre 20,000 y 50,000, es del 10%, y si supera los 50,000, es del 15%.

salario = float(input("Ingrese el salario: "))

if salario <= 20000:
    impuesto = salario * 0.05
elif salario <= 50000:
    impuesto = salario * 0.1
else:
    impuesto = salario * 0.15

print("El impuesto es:", impuesto)