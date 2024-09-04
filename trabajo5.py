Total_pesos = {"niños": 0, "jóvenes": 0, "adultos": 0, "ancianos": 0}
Conteo = {"niños": 0, "jóvenes": 0, "adultos": 0, "ancianos": 0}
for _ in range(5):
 Edad = int(input("Ingrese la edad de la persona: "))
 Peso = float(input("Ingrese el peso de la persona: ")) 
if Edad <= 12:
 Total_pesos["niños"] += Peso
 Conteo["niños"] += 1
elif Edad <= 29:
 Total_pesos["jóvenes"] += Peso
 Conteo["jóvenes"] += 1
elif Edad <= 59:
 Total_pesos["adultos"] += Peso
 Conteo["adultos"] += 1
else:
 Total_pesos["ancianos"] += Peso
 Conteo["ancianos"] += 1
for grupo, total_peso in Total_pesos.items():
 if Conteo[grupo] > 0:
  print(f"Promedio de peso de {grupo}: {total_peso / Conteo[grupo]} kg")
