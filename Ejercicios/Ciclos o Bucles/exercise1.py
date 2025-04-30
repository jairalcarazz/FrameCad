no = 1
while no > 0:
    # Este programa verifica si un número es positivo o negativo
    # y solicita al usuario que ingrese un número.
    # Si el número es negativo, se termina el ciclo.
    no = int(input("Ingrese un numero: "))
    print(f"El cuadrado del numero es:{no*no} ")
if no<=0:   
    print("El numero es negatico ")

print("Fin del programa")