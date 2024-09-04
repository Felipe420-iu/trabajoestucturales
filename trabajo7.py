# Aca se determina cuántos autos entran a Ibagué con calcomanías de cada color
# basado en el último dígito de la placa.
amarillo = 0
rosa = 0
roja = 0
verde = 0
azul = 0
n = int(input("Ingrese la cantidad de autos que entraron: "))

for _ in range(n):# Se usa un ciclo para leer el último dígito de la placa de cada auto
    placa = input("Ingrese el último dígito de la placa: ")
    ultimo_digito = int(placa[-1])
    if ultimo_digito == 1 or ultimo_digito == 2: # Se determina el color de la calcomanía según el último dígito de la placa
        amarillo += 1
    elif ultimo_digito == 3 or 4:
        rosa += 1
    elif ultimo_digito == 5 or 6:
        roja += 1
    elif ultimo_digito == 7 or 8:
        verde += 1
    elif ultimo_digito == 9 or 0:
        azul += 1

# Se imprimen los resultados
print(f"Calcomanía amarillo: {amarillo}")
print(f"Calcomanía rosa: {rosa}")
print(f"Calcomanía roja: {roja}")
print(f"Calcomanía verde: {verde}")
print(f"Calcomanía azul: {azul}")
