diccionario = {
    "nombre": "lucas",
    "apellido": "Dalto",
    "subs" : 100000
}

#recorriendo diccionariopara obtener las claves 

for key in diccionario:
    key
    print(f'la clave es :{key}')
    

#recorriendo diccionario con items() para obtener la clave y el valor

for datos in diccionario.items():
    key = datos[0]
    value = datos [1]
    print(f'la clave es :{key} y el valor es: {value}')
    