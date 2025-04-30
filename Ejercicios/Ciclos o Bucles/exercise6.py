numero = 1
suma_de_numeros = 0
while numero != 0:
    numero = int(input("Ingrese un número (0 para salir): "))
    suma_de_numeros += numero
    
    if numero == 0:
        print(f"La suma de los numeros que ingresaste es: {suma_de_numeros} \n Saliendo del programa..")
    else:
        print(f"El número ingresado es: {numero}")