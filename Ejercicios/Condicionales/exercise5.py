horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
horas_semanales = 40
sueldo_base = 16
sueldo_extra = 20
if horas_trabajadas > horas_semanales:
    h = horas_semanales*sueldo_base
    horas_extra = horas_trabajadas-horas_semanales
    pago_extra = horas_extra*sueldo_extra
    total = h + pago_extra
    
else:
    total = horas_trabajadas*sueldo_base

print("El salario total es", total)

