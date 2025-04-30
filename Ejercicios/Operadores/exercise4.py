


calificacion_participacion = int(input("Calificacion de participacion: "))
calificacion_examen1 = int(input("Calificacion de examen: "))
calificacion_examen2 = int(input("Calificacion de examen 2: "))
calificacion_examen_final = int(input("Calificacion de examen final: "))

participacion = 10*calificacion_participacion/10
examen1 = 25*calificacion_examen1/10
examen2 = 25*calificacion_examen2/10
examen_final = 40*calificacion_examen_final/10

calificacion_final = participacion + examen1 + examen2 + examen_final
print(f"Tu calificacion final es: {calificacion_final}")

