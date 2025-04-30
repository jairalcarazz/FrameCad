nota = int(input("Ingrese una nota: "))

if nota < 6:
    print ("es insuficiente")
elif nota < 8:
    print ("es suficiente")
elif nota < 9:
    print("es notable")
elif nota <11:
    print ("Es sobresaliente")
    
else: 
    print("nota no valida")