#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando conventirlos a entero y sumarlos
        try:  
            resultado = int(a) + int(b)
        #si lanza una excepcion pedirle que reingrese los datos
        except:
            print("Te  pedi iun numero")
        #si todo salio bien se termina el bucle
        else:
            break
        finally:
            print("manejo de excepcion finalizado")
     
    #mostrando el resultado
    return resultado  

print(sumar_dos())