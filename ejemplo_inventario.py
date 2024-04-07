#Extraer datos
from inventario import Inventario

#Creacion del objeto
paquete01 = Inventario("antiinflamatorios", 10)

#Modificar datos
paquete01.set_cantidad(34)

#Mostrar datos actualizados
print("gracias por traernos este nuevo paquete de:",paquete01._remedios)
print("con esto ahora poseemos una cantidad de:",paquete01.get_cantidad(),"en cajas")