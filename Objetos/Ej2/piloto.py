from persona import Persona

class Piloto(Persona):

    def __init__(self,casa,coche,dinero,puntuacion):
        super().__init__(casa,coche,dinero)
        self.puntuacion = puntuacion

    
    @property
    def puntuacion(self):
        return self.__puntuacion
    
    @puntuacion.setter
    def puntuacion(self,puntuacion):
        self.__puntuacion = puntuacion

    
    def mostrar(self):
        return "\nPiloto: " + super().mostrar() + "\nPuntuacion: " + str(self.puntuacion)
    
    def estaEnDescenso(self):
        return self.puntuacion < 100