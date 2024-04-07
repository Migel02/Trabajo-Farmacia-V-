#importar matematicas
import math

#Creacion de la clase 
class Inventario:
    def __init__(self, remedios, cantidad):
       #Atributos del Inventario
        self._remedios = remedios
        self._cantidad = cantidad

    #Mutadores de
    def set_cantidad(self, nueva_cantidad):
        self._cantidad = (nueva_cantidad + self._cantidad)
    
    def set_remedios(self, nuevo_remedios):
        self._remedios = nuevo_remedios

    #accesadores
    def get_cantidad(self):
        return self._cantidad
    
    def get_remedios(self):
        return self._remedios
    