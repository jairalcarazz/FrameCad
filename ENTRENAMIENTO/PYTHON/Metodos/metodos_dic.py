diccionario = {
    "nombre" : "Lucas"
    "apellido" : "Dalto"
    "subs" : 100000
}
claves = diccionario.keys()

print(claves) 


#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo el valor con get si no lo encuentra el programa continua si no aventara error
valor_de_kajs = diccionario.get("kajs")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("Nombre")

#obteniendo un elememnto dirct_item iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)