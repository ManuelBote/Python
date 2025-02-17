# Crea una clase Vehículo con un atributo marca. Luego, crea las subclases
# Coche y Camión, cada una con un atributo adicional (por ejemplo, puertas y
# capacidad respectivamente)

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Coche(Vehiculo):
    def __init__(self, marca, puertas, capacidad):
        super().__init__(marca)
        self.puertas = puertas
        self.capacidad = capacidad

    def mostrar(self):
        print("Coche: " + self.marca + " con " + str(self.puertas) + " puertas y " + str(self.capacidad) + " de capacidad")

class Camion(Vehiculo):
    def __init__(self, marca, puertas, capacidad):
        super().__init__(marca)
        self.puertas = puertas
        self.capacidad = capacidad

    def mostrar(self):
        print("Camión: " + self.marca + " con " + str(self.puertas) + " puertas y " + str(self.capacidad) + " de capacidad")


c1 = Coche("Audi", 4, 4)
c1.mostrar()

c2 = Camion("Mercedes", 2, 2)
c2.mostrar()