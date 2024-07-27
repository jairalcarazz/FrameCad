#creando una funcion que nos regrese los numero primos
#entre el 0 y el argumento que pasamos

#creamos una funcion que verifique si el numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse por ningun numero entre 2
    #y el mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
        #si temrina el bucle , significa que no fue divisible y es primo
    return True

#Creando funcion que retome una lista con todos los primos
def primos_hasta(num):
    #creamos una lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #emn caso de que lo sea lo agregamos a la lista
        if resultado == True: primos.append(i)
        #devolvemos la lista
    return primos

resultado = primos_hasta(132)

print(resultado)
        
        