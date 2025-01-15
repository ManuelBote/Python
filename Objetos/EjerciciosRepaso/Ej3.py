# Crea una clase Persona con el atributo nombre. 
# Añade un método saludar que imprima "Hola, soy [nombre]". Luego, crea un objeto de esta clase e invoca el método

class Persona: 
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print("Hola, soy " + self.nombre)

p1 = Persona(input("Nombre: "))
p1.saludar()