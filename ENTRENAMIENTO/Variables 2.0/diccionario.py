#creando un diccionario con dict()
diccionario = dict(nombre="lucad", apellido="dalto")

#las listas no pueden ser claves 
diccionario = {frozenset(["dalto", "rancio"]):"jajas"}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido","suscriptores"])

print(diccionario) 


#parentesis son tuplas y corchetes son listas, llaves son conjuntis {}
 