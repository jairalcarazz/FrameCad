#falto el profe y los pibes van a armar la clase.

#funcion para obtener el asistente y el profesor segun la edad.
def obtener_compañeros(cantidade_de_compañeros):
    
    #creando lsta de compañeros
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidade_de_compañeros):
        nombre = input("Ingrese el nombre del compañero:  ")
        edad = int(input("Ingrese la edad del compañero:  "))
        compañero = (nombre,edad)
        
        #agregando la informaciona a la lista
        compañeros.append(compañero)
    
    #ordenandolos de menor a mayor segun su edad
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nomobre,edad) y despues accedemos al nombre
    #para definir al asistente y el profesor
    
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)

#mostrar el resultado
print(f"El profesor es: {profesor} y su asistente es {asistente}")


    