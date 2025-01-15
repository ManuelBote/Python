def calcularVuelta(dinero, cantidad):
    vuelta = dinero // cantidad
    dinero = dinero - vuelta*cantidad
    return vuelta, dinero

cantidades = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]

def EscribirVuelta(vuelta, cantidad): #nº de billetes, valor de billetes
    if vuelta > 0:
        if cantidad > 2:
            print(vuelta,"billetes de",cantidad,"€")
        else:
            if cantidad >= 1:
                print(vuelta,"monedas de",cantidad,"€")
            else:
                print(vuelta,"monedas de",cantidad*100,"centimos")


total = float(input("Indique el total a pagar: "))
entregado = float(input("Indica el dinero entregado: "))
dinero = entregado - total

for i in cantidades:
    vuelta, dinero = calcularVuelta(dinero, i)
    EscribirVuelta(vuelta, i)