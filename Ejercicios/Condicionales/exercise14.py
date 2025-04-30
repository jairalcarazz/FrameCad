numero = 1
while numero != 0:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        print("Saliendo del programa...")
    else:
        print(f"El número ingresado es: {numero}")