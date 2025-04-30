no = 1
no_de_no = 0

while no != 0:
    no = int(input("Ingrese un numero: "))
    no_de_no += 1
    if no == 0:
        print("Saliendo del programa...")
    

print ("ingresaste un total de ", no_de_no-1, " numeros")
print ("Fin del programa")