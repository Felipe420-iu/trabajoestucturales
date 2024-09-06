nota1 = float(input("introduce la nota1: "))
nota2 = float(input("introduce la nota2: "))
nota3 = float(input("Introduce la nota3: "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 70:
    print(f"El aprendiz del sena aprueba con un promedio de {promedio:.2f}.")
else:
    print(f"El aprendiz del sena desaprueba con un promedio de {promedio:.2f}.")

