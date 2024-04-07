#Extraer datos
from cita import Cita

#Creacion del objeto
cliente01 = Cita("Carlitos Gonzales","dolor abdominal","9:45")

#Modificar datos
cliente01.set_hora("10:20")

#Mostrar datos actualizados
print("disculpenos porfavor señor:",cliente01._nombre)
print("por un error tuvimos que cambiar su pedido a las",cliente01.get_hora(),"horas")