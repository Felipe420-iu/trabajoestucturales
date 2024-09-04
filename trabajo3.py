Calificaciones = [] 
for _ in range(20):
 Calificacion = float(input("Ingrese la calificación del alumno: ")) 
 Calificaciones.append(Calificacion) 
Promedio = sum(Calificaciones) / len(Calificaciones)
Calificacion_max = max(Calificaciones)
Calificacion_min = min(Calificaciones)
print(f"Promedio: {Promedio}, Máxima: {Calificacion_max}, Mínima:
{Calificacion_min}")