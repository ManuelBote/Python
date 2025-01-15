class Pantalla:
    def __init__(self, tamaño, resolucion):
        self.tamaño = tamaño
        self.resolucion = resolucion

    def __str__(self):
        return f"Pantalla: {self.tamaño}, {self.resolucion}"


class Camara:
    def __init__(self, megapixeles, apertura):
        self.megapixeles = megapixeles
        self.apertura = apertura

    def __str__(self):
        return f"Camara: {self.megapixeles}MP, {self.apertura}"


class Hardware:
    def __init__(self, procesador, ram):
        self.procesador = procesador
        self.ram = ram

    def __str__(self):
        return f"Hardware: {self.procesador}, {self.ram}GB RAM"


class Bateria:
    def __init__(self, capacidad, tipo):
        self.capacidad = capacidad
        self.tipo = tipo

    def __str__(self):
        return f"Bateria: {self.capacidad}mAh, {self.tipo}"



class Movil:
    def __init__(self, pantalla, camara, hardware, bateria):
        self.pantalla = pantalla
        self.camara = camara
        self.hardware = hardware
        self.bateria = bateria

    def __str__(self):
        return (f"Movil con: \n{self.pantalla}\n"
                f"{self.camara}\n"
                f"{self.hardware}\n"
                f"{self.bateria}")


pantalla = Pantalla("6.5 pulgadas", "1080x2400")
camara = Camara(48, 1.8)
hardware = Hardware("SnapDragon", 8)
bateria = Bateria(5000, "Li-Ion")

movil = Movil(pantalla, camara, hardware, bateria)

print(movil)
