#creacion de la clase
class Cita:
    def __init__(self, nombre, razon, hora):
         #Atributos 
        self._nombre = nombre
        self._razon = razon
        self._hora = hora

    #mutadores
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    def set_razon(self, nuevo_razon):
        self._razon = nuevo_razon

    def set_hora(self, nuevo_hora):
        self._hora = nuevo_hora

    #accesadores
    def get_nombre(self):
        return self._nombre
    
    def get_razon(self):
        return self._razon
    
    def get_hora(self):
        return self._hora