#creando una funcion de tres parametros

#def frase(nombre,apellido,adjetivo)
#   return f"Hola{nombre} {apellido}, sos muy {adjetivo}"

#utilizando keyboard arguments
#frase_resultante = frase(adjetivo = 'capo', nombre = 'Lucas', apellido = "Dslto")


#creando la misma duncion con un parametro opcional
def frase(nombre,apellido,adjetivo = "Tonto"):
    return f"Hola{nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase("Lucas","Dalto","Inteligente")
print(frase_resultante)