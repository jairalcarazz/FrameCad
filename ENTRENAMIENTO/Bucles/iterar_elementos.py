animales = [ "gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72]

#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

#recorriendo la lista numeros  y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
  
 
#iterando dos listas del mismo tamaño al mismo tiempo       
for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')

#si no ponemos un rango de inicio empieza desde cero hasta el numero indicado
for num in range(5,10):
    print(num)
    
#forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])

#forma correcta de recorrer una liste con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num [1]
    print(f'el indice es :{indice} y el valor es: {valor}')
    
    #usando el else
    for numero in numeros:
        print(f"ejecutando el ultimo bucle , valor actual: {numero}")
    else:
        print ("el bucle termino")
        
    #todo lo anterior funciona exactamente igual para tuplas
    