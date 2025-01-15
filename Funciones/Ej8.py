# Crea un programa principal que permita convertir de decimal a binario y de binario a decimal
def hacerBinario(dec):
    bin = ""
    while dec > 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return bin

def hacerDecimal(bin):
    dec = 0
    n = len(str(bin))-1
    for i in range (len(str(bin))):
        dec += int(str(bin)[n]) * 2**i
        n -= 1
    return dec


dec = int(input("Introduce un decimal: "))
bin = int(input("Introduce un binario: "))

print("El binario de",dec,"es",hacerBinario(dec))
print("El decimal de",bin,"es",hacerDecimal(bin))
