no = 1

while no!=0:
    no = int(input("Ingrese un numero: "))
    if no % 2 == 0:
        print("El numero es par")
    else:
        print("el numero es impar")
        
    if no ==0:
        print("Saliendo del programa...")