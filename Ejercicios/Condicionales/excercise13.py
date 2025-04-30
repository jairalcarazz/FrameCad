saldo = 1000
print (f"Su saldo es de {saldo}")

operacion = int(input("Que operacion desea realizar:\n 1.Ingresar dinero\n 2. Retirar dinero\n 3. Salir\n"))
if operacion == 1:
    dineroingresado = int(input("Cuanto dinero quiere ingresar?"))
    nuevosaldo = saldo + dineroingresado
    
    print(f"Su saldo es de {nuevosaldo}")
    
elif operacion == 2:
    dineroretirado = int(input("Cuanto dinero desea retirar? "))
    nuevosaldo = saldo - dineroretirado
    print(f"Su saldo es de {nuevosaldo}")
elif operacion == 3:
    print("Gracias por usar el cajero")
else:
    print("Operacion no valida")

    
    
    