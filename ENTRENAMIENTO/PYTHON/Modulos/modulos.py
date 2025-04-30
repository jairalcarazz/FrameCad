#importanto un modulo y  asignando el nombre m_saludar
#import modulo_saludar as m_saludar

#donde ese modulo se importan dos funciones del modulo anterior
# Y se les puede cambiar el nombre como en el ejemplo
from modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_como_coscu

#Creamos las variables con los saludos
saludo = saludar_normal("Lucas")
saludo_raro = saludar_como_coscu("Fran")

#mostrar los resultados
print(saludo)
print(saludo_raro)