class Persona():

    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad

    #GETTERS
    @property
    def dni(self):
        return self.__dni

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    #SETTERS
    @dni.setter
    def dni(self, dni):
        self.__dni = dni
        self.validar_dni()

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad = 0
        else:
            self.__edad = edad



    def validar_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        if len(self.__dni) != 9:
            print("DNI Incorrecto")
            self.__dni = ""
        else:
            letra = self.__dni[8]
            num = int(self.__dni[:8])
            if letra.upper() != letras[num%23]:
                print("DNI Incorrecto")
                self.__dni = ""
        

    def mostrar(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nDNI: {self.dni}"