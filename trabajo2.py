Suma_positivos = 0
for _ in range(10):
 Numero = int(input("Ingrese un número negativo:"))
if Numero < 0:
 Suma_positivos += abs(Numero) 

print(f"Suma de los números positivos: {Suma_positivos}")
