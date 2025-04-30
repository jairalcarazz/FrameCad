salario_por_hora = 12
horas = 0
for i in range (1,6):
    h = float(input(f"Cuantas horas trabajaste el dia {i}: "))
    horas += h
    
print(f"El salario semanal es: {horas * salario_por_hora}")
