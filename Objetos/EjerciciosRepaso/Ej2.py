# Crea una clase Coche con atributos marca, modelo, año y color. Agrega un constructor que inicialice estos atributos. 
# Crea un objeto de esta clase y muestra sus atributos.

class Coche:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
    
    def mostrar(self):
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Año: " + str(self.año))
        print("Color: " + self.color)

c1 = Coche("Audi", "A4", 2020, "Blanco")
c1.mostrar()