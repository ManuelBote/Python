class DNI():

    def __init__(self, numero):
        self.numero = numero

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def dni(self, numero):
        self.__numero = numero
        self.validar_dni()


    def validar_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.__numero) != 9:
            print("DNI Incorrecto")
            self.__numero = ""
        else:
            letra = self.__numero[8]
            num = int(self.__numero[:8])
            if letra.upper() != letras[num%23]:
                print("DNI Incorrecto")
                self.__numero = ""


    def mostrar(self):
        print(self.numero)


dni = DNI("12345678A")
dni.mostrar()