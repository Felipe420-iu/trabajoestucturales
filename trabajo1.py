Positivos = 0 
Negativos = 0 
Neutros = 0
for  i in range(20):
    numero = int( input("Ingrese un número: "))
if numero > 0:
    Positivos += 1
elif numero < 0:
 Negativos += 1 
else:
 Neutros += 1 
print(f"Positivos: {Positivos}, Negativos: {Negativos}, Neutros: {Neutros}")

