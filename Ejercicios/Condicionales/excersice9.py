dia = int(input("Ingrese día: "))
mes = int(input("Ingrese mes: "))
ano = int(input("Ingrese año: "))

if (dia > 0 and dia <= 31) and (mes > 0 and mes <= 12) and (ano > 0):
    print("La fecha es correcta")
else:
    print("La fecha es incorrecta")

print("La fecha es:", dia, "/", mes, "/", ano)
