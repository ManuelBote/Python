# Escribe un programa que determine si una persona puede pagar la cuota
# mensual de un préstamo según su salario. Si la cuota es menor al 30% del
# salario, es "asequible", de lo contrario, es "no asequible".

salario = float(input("Ingrese el salario: "))
cuota = float(input("Ingrese la cuota mensual: "))

if cuota <= salario * 0.3:
    print("Es asequible")
else:
    print("No es asequible")    