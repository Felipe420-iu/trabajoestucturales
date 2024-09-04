# Este programa clasifica las calificaciones de 23 estudiantes en diferentes rangos.
menos_50 = 0
entre_50_69 = 0
entre_70_79 = 0
mas_80 = 0
for _ in range(23): # Se usa un ciclo para leer la calificación de cada estudiante
    calificacion = int(input("Ingrese la calificación del estudiante (1-100): "))
    

    if calificacion < 50: # Se clasifica la calificación en el rango correspondiente
        menos_50 += 1
    elif 50 <= calificacion < 70:
        entre_50_69 += 1
    elif 70 <= calificacion < 80:
        entre_70_79 += 1
    else:
        mas_80 += 1

# Se imprimen los resultados
print(f"Estudiantes con calificación menor a 50: {menos_50}")
print(f"Estudiantes con calificación entre 50 y 69: {entre_50_69}")
print(f"Estudiantes con calificación entre 70 y 79: {entre_70_79}")
print(f"Estudiantes con calificación de 80 o más: {mas_80}")