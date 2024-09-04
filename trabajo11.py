Hombres = 0 
Mujeres = 0
Altura_total = 0
Conteo_total = 0 
Mayores_170 = 0 
Menores_igual_150 = 0
while True:
    
    edad = int(input("Ingrese la edad del alumno (0 para finalizar): ")) 
    if edad == 0:
      
        break
sexo = input("Ingrese el sexo (H/M): ").upper()
altura = float(input("Ingrese la altura en metros: ")) 
Conteo_total += 1 
Altura_total += altura 
if sexo == "H":
 
 Hombres += 1
elif sexo == "M":
 Mujeres += 1
if altura > 1.70:
 Mayores_170 += 1
elif altura <= 1.50:
 Menores_igual_150 += 1
Promedio_altura = Altura_total / Conteo_total if Conteo_total > 0 else 0
print(f"Hombres: {Hombres}")
print(f"Mujeres: {Mujeres}")
print(f"Altura promedio: {Promedio_altura:.2f} metros")
print(f"Alumnos con altura mayor a 1.70m: {Mayores_170}")
print(f"Alumnos con altura menor o igual a 1.50m: {Menores_igual_150}")