
class Coche():

    def __init__(self, matricula, marca, kilometraje):
        self.matricula = matricula
        self.marca = marca
        self.kilometraje = kilometraje

    #GETTERS
    @property
    def matricula(self):
        return self.__matricula

    @property
    def marca(self):
        return self.__marca
    
    @property
    def kilometraje(self):
        return self.__kilometraje
    
    #SETTERS
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @kilometraje.setter
    def kilometraje(self, kilometraje):
        self.__kilometraje = kilometraje


    def mostrarDatos(self):
        return f"Matricula: {self.matricula}\nMarca: {self.marca}\nKilometraje: {self.kilometraje}"
    
    def segundaMano(self):
        return self.kilometraje > 27000
    


# coche1 = Coche("1234ABC","Opel",150000)
# datos = coche1.mostrarDatos()
# print(datos)
