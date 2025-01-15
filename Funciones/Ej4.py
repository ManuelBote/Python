#Crea un programa principal que al introducir una fecha nos diga, el dia juliono que es

def julian (dia, mes, año):
    dj = (365.25*(año+4716)+30.6001*(mes+1)+dia+2-(año/100)+((año/100)/4)-1524.5)
    return dj


dia = int(input("Indica el dia: "))
mes = int(input("Indica el mes: "))
año = int(input("Indica el año: "))

dj = julian(dia, mes, año)
print("El dia juliano es:",dj)