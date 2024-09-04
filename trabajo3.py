suma_calificaciones = 0 # Se calcula el promedio, la calificación más alta y más baja de un grupo de 20 alumnos.
calificacion_max = float('-inf')  # Usamos un valor muy bajo para inicializar la máxima calificación
calificacion_min = float('inf')  # Usamos un valor muy alto para inicializar la mínima calificación
for _ in range(20): # Se usa un ciclo para leer las 20 calificaciones
    calificacion = float(input("Ingrese la calificación del alumno: "))  # Se lee la calificación del alumno
    suma_calificaciones += calificacion  # Se suma la calificación a la suma total
    if calificacion > calificacion_max:
        calificacion_max = calificacion
    if calificacion < calificacion_min:
        calificacion_min = calificacion # Se verifica si la calificación actual es la más alta o más baja
promedio = suma_calificaciones / 20 # Se calcula el promedio}
print(f"Promedio: {promedio}, Máxima: {calificacion_max}, Mínima: {calificacion_min}") # Se imprimen los resultados