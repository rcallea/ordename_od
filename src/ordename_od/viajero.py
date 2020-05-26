class Viajero:

    def __init__(self, nombre, apellido, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo

    def __str__(self):
        return self.nombre + " " + self.apellido + " (" + self.correo + ")"

    def __eq__(self, otro_viajero):
        if not isinstance(otro_viajero, Viajero):
            return NotImplemented

        return self.id == otro_viajero.id and self.nombre == otro_viajero.nombre and self.apellido == otro_viajero.apellido and self.correo == otro_viajero.correo

    def get_nombre(self):
        return(self.__nombre)

    def set_nombre(self, nombre):
        self.__nombre = nombre