import random

intento = 1
no_de_intentos = 0
numero = random.randint(1, 100)  # Genera un número entero entre 1 y 100
while intento != numero:
    intento  = int(input("Adivina el numero: "))
    if intento < numero:
        print("el intento es menor")
        no_de_intentos += 1
    elif intento > numero: 
        print("el intento es mayor")
        no_de_intentos += 1
    else:
        print("Ganeste jotito, lo intentaste",no_de_intentos)
        break
    if intento == numero:
        print("Ganaste")
    
