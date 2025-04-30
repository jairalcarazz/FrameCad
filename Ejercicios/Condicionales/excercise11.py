operation = input("Inserte la operacion: ").lower()
numero_1 = int(input("Inserte el primer numero: "))
numero_2 = int(input("Inserte el segundo numero numero: "))

if operation == "s":
    resultado = numero_1 + numero_2
    print("el resultado es", resultado)
    
elif operation == "r":
    resultado = numero_1 - numero_2
    print("el resultado es", resultado)

elif operation == "m":
    resultado = numero_1 * numero_2
    print("el resultado es", resultado)

elif operation == "d":
    resultado = numero_1 / numero_2
    print("el resultado es", resultado)

else:
    print("operacion no valida")
    


