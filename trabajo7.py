N = int(input("Ingrese la cantidad de autos que entraron: "))
Calcomanias = {"amarillo": 0, "rosa": 0, 
               "roja": 0, "verde": 0, 
               "azul": 0} 

for _ in range(N):
    Placa = input("Ingrese el último dígito de la placa: ")
    ultimo_digito = int(Placa[-1])
    if ultimo_digito == 1 or ultimo_digito == 2:
        Calcomanias["amarillo"] += 1
    elif ultimo_digito == 3 or ultimo_digito == 4:
        Calcomanias["rosa"] += 1
    elif ultimo_digito == 5 or ultimo_digito == 6:
        Calcomanias["roja"] += 1
    elif ultimo_digito == 7 or ultimo_digito == 8:
        Calcomanias["verde"] += 1
    elif ultimo_digito == 9 or ultimo_digito == 0:
        Calcomanias["azul"] += 1

for color, cantidad in Calcomanias.items():
 print(f"Calcomanía {color}: {cantidad}")
