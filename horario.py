#Creacion de la clase
class Horario:
    def __init__(self, nombre, cargo, horas, dias):
         #Atributos 
        self._nombre = nombre
        self._cargo = cargo
        self._horas = horas
        self._dias = dias

    #mutadores
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_cargo(self, nuevo_cargo):
        self._cargo = nuevo_cargo
        
    def set_horas(self, nuevo_horas):
        self._horas = nuevo_horas
    
    def set_dias(self, nuevo_dias):
        self._dias = nuevo_dias

    #accesadores
    def get_nombre(self):
        return self._nombre
    
    def get_cargo(self):
        return self._cargo
    
    def get_horas(self):
        return self._horas
    
    def get_dias(self):
        return self._dias