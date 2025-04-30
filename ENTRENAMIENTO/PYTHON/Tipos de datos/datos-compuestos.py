lista = ["Lucas","Soy Dalto",True, 1.85]
tupla = ["Lucas","Soy Dalto",True, 1.85]
print(lista[1])
#tupla no se puede modificar y las listas si. Conjuntos no tienen orden.
#esto es valido para modificar un dato en una lista
lista[3] = "Marisola"
print(lista)
#Esto no es posible
#tupla[3] = "Marisola"

#Creando un conjunto (set) (no se accede a elementos por indice, no almacena dastos duplicados)
conjunto = {"Lucas Dalto","Soy Dalto", True,1.85, "Soy Dalto" }

#print(conjunto[3]) - no se puede acceder al elemento por el conjunto

#Creando un diccionario (dict) la estructura es key : value y se separan con comas 
diccionario = {
    'nombre' : "Lucas Dalto",
    'canal' : "Soy Dalto",
    'estaemocionado' : True,
    'altura' : 1.84,
    'dato duplicado' : "Soy Dalto"
    }

print(diccionario['altura'])