suma_edad_hombres = 0
conteo_hombres = 0
suma_edad_mujeres = 0
conteo_mujeres = 0
n = int(input("Ingrese el número total de alumnos: "))
for _ in range(n):
    sexo = input("Ingrese el sexo (H/M): ").upper() 
    edad = int(input("Ingrese la edad: "))  
    
    if sexo == "H":
        suma_edad_hombres += edad  
        conteo_hombres += 1  
    elif sexo == "M":
        suma_edad_mujeres += edad  
        conteo_mujeres += 1  
promedio_hombres = suma_edad_hombres / conteo_hombres if conteo_hombres > 0 else 0
promedio_mujeres = suma_edad_mujeres / conteo_mujeres if conteo_mujeres > 0 else 0
promedio_total = (suma_edad_hombres + suma_edad_mujeres) / (conteo_hombres + conteo_mujeres) if (conteo_hombres + conteo_mujeres) > 0 else 0
print(f"Promedio de edad de hombres: {promedio_hombres:.2f}")
print(f"Promedio de edad de mujeres: {promedio_mujeres:.2f}")
print(f"Promedio de edad de todo el grupo: {promedio_total:.2f}")