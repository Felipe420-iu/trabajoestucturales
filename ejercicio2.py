cantidad_zapatillas = int(input("ingrese cuantas zapatillas compro: "))
precio_mercado = float(input("Ingrese el precio unitario de las zapatillas: "))
valor_compra = cantidad_zapatillas * precio_mercado
if cantidad_zapatillas >= 3:
    descuento = 0.20 
    print(f"el descuento por:{cantidad_zapatillas} zapatillas es de, {valor_compra} mil pesos")
else:
    descuento = 0.10 
    print(f"el descuento por,{cantidad_zapatillas} zapatillas es de, {valor_compra} mil pesos")
valor_descuento = valor_compra * descuento
valor_final = valor_compra - valor_descuento
print(f"Valor de la compra es de: ${valor_compra:.2f}")
print(f"Valor del descuento es de: ${valor_descuento:.2f}")
print(f"Valor a pagar después del descuento: ${valor_final:.2f}")

