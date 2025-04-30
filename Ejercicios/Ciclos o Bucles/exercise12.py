#pedir un numero y calcular el factorial
numero = int(input("Ingrese un número: "))
factorial = 1
for i in range (1,numero+1):
    factorial  *= i
print(f"El factorial de {numero} es: {factorial}")  