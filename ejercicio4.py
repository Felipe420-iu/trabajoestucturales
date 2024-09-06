import random
total_compra = float(input("Ingresa el valor total de la compra: $"))
colores = ["rojo", "verde", "otros"]
color_balota = random.choice(colores)
if color_balota == "rojo":
    descuento = 0.15 
elif color_balota == "verde":
    descuento = 0.20
else:
    descuento = 0.00 
valor_descuento = total_compra * descuento
valor_final = total_compra - valor_descuento
print(f"Color de la balota: {color_balota}")
print(f"Valor de la compra: ${total_compra:}")
print(f"Descuento aplicado: ${valor_descuento:}")
print(f"Valor final a pagar: ${valor_final:}")