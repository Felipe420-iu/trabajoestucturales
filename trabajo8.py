
Calificaciones = {"<50": 0, "50-69": 0, "70-79": 0, "80+": 0}
for _ in range(23):
 Calificacion = int(input("Ingrese la calificación del estudiante (1-100): ")) 
if Calificacion < 50:
 Calificaciones["<50"] += 1
elif 50 <= Calificacion < 70:
 Calificaciones["50-69"] += 1
elif 70 <= Calificacion < 80:
 Calificaciones["70-79"] += 1
else:
 Calificaciones["80+"] += 1
for rango, cantidad in Calificaciones.items():
 print(f"Estudiantes en el rango {rango}: {cantidad}")