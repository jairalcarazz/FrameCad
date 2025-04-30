#crear un programa que me arroje el numero de semanas dias y horas de un numero de horas dado por el usuario

numero_de_horas = int(input("ingrese el numero total de horas:"))
semana = 168
dia = 24
hora = 1
semanas = numero_de_horas // semana
dias = (numero_de_horas % semana)//dia
horas =(numero_de_horas %dia)//hora
print(f"el numero de semanas es: {semanas} \n el numero de dias es {dias}\n el numero de horas es {horas}")

