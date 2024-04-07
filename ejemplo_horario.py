#Extraer datos
from horario import Horario

#Creacion del objeto
persona01 = Horario("javier Diaz","bodeguero","9:30 a 17:00","lunes a jueves")

#Modificar datos 
persona01.set_nombre("Constanza Alarcon")
persona01.set_dias("martes")
persona01.set_horas("12:00 a 13:20")

#Mostrar datos actualizados
print(persona01.get_nombre())
print("podrias cubrir a tu compañero el dia",persona01.get_dias(),"a las",persona01.get_horas(),"horas")
print("tiene una emergencia a esa hora y necesito a alguien que lo cubra en su puesto de",persona01.get_cargo())