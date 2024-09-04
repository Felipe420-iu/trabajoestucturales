N = int(input("Ingrese el número de personas en el salón: ")) 
Hombres = 0 
Mujeres = 0 
for _ in range(N):
 Sexo = input("Ingrese el sexo (H/M): ").upper() 
if Sexo == "H":
 Hombres += 1 
elif Sexo == "M":
 Mujeres += 1
print(f"Hombres: {Hombres}, Mujeres: {Mujeres}")
