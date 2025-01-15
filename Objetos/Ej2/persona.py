from coche import Coche

class Persona():

    def __init__(self,casas,coche,dinero):
        self.casas = casas
        self.coche = coche
        self.__dinero = dinero


    #GETTERS
    @property
    def casas(self):
        return self.__casas
    
    @property
    def coche(self):
        return self.__coche
    
    @property
    def dinero(self):
        return self.__dinero
    
    #SETTERS
    @casas.setter
    def casas(self, casas):
        self.__casas = casas

    @coche.setter
    def coche(self, coche):
        self.__coche = coche



    def mostrar(self):
        return "\nIndividuo: \n-Casa: " + str(self.casas) + "\n-Coche: " + self.coche.mostrarDatos() + "\n-Dinero: " + str(self.dinero)
    
    def disminuir(self, dinero):
        if dinero > 0:
            self.__dinero -= dinero




p1 = Persona("casas1", Coche("1234ABC","Opel",200909),1300)
print(p1.mostrar())
p1.disminuir(100)
print(p1.mostrar())
