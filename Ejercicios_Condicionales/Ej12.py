# Escribe un programa que reciba un número de mes (1-12) y determine
# cuántos días tiene (considerando años no bisiestos)

mes = int(input("Ingrese el número del mes: "))

dia = 0

if mes == 1:
    dias = 31
elif mes == 2:
    dias = 28
elif mes == 3:
    dias = 31
elif mes == 4:
    dias = 30
elif mes == 5:
    dias = 31
elif mes == 6:
    dias = 30
elif mes == 7:
    dias = 31
elif mes == 8:
    dias = 31
elif mes == 9:
    dias = 30
elif mes == 10:
    dias = 31
elif mes == 11:
    dias = 30
elif mes == 12:
    dias = 31
else:
    print("El número no es correcto")

if dia != 0:
    print("Los", dias, "días de", mes, "meses tienen", dias, "días")