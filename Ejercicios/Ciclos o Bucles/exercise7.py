numero = 0
no_de_no = 0
suma_total = 0

while numero >= 0:
    numero = int(input("Ingresa un numero: "))
    suma_total += numero
    no_de_no += 1
    media = suma_total / no_de_no
    
    if numero < 0:
        print(f" El promedio de los numeros ingresados es: {media}\nSaliendo del programa...")
