# Se determina el promedio de peso de niños, jóvenes, adultos y viejos.
suma_peso_ninos = 0
conteo_ninos = 0
suma_peso_jovenes = 0
conteo_jovenes = 0
suma_peso_adultos = 0
conteo_adultos = 0
suma_peso_viejos = 0
conteo_viejos = 0
for _ in range(10):# Se usa un ciclo para leer la edad y peso de 10 personas
    edad = int(input("Ingrese la edad de la persona: "))
    peso = float(input("Ingrese el peso de la persona: "))
    if edad <= 12: # Se determina el grupo de edad al que pertenece la persona
        suma_peso_ninos += peso
        conteo_ninos += 1
    elif edad <= 29:
        suma_peso_jovenes += peso
        conteo_jovenes += 1
    elif edad <= 59:
        suma_peso_adultos += peso
        conteo_adultos += 1
    else:
        suma_peso_viejos += peso
        conteo_viejos += 1
if conteo_ninos > 0:# Se calcula y se muestra los promedios, verificando que el conteo no sea cero
    print(f"Promedio de peso de niños: {suma_peso_ninos / conteo_ninos} kg")
if conteo_jovenes > 0:
    print(f"Promedio de peso de jóvenes: {suma_peso_jovenes / conteo_jovenes} kg")
if conteo_adultos > 0:
    print(f"Promedio de peso de adultos: {suma_peso_adultos / conteo_adultos} kg")
if conteo_viejos > 0:
    print(f"Promedio de peso de ancianos: {suma_peso_viejos / conteo_viejos} kg")
