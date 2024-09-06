monto_compra = float(input("Ingresa el total de la compra: $"))
if monto_compra > 500000:
    inversion_propia = monto_compra * 0.55
    prestamo_banco = monto_compra * 0.30
    credito_fabricante = monto_compra - (inversion_propia + prestamo_banco)
    print(f"Inversión propia de la empresa: ${inversion_propia:}")
    print(f"Préstamo del banco: ${prestamo_banco:}")
    print(f"Crédito solicitado al fabricante: ${credito_fabricante:}")
else:
    inversion_propia = monto_compra * 0.70
    prestamo_banco = 0 
    credito_fabricante = monto_compra * 0.30
intereses_fabricante = credito_fabricante * 0.20
total_credito = credito_fabricante + intereses_fabricante
print(f"Inversión propia de la empresa: ${inversion_propia:}")
print(f"Préstamo del banco: ${prestamo_banco:}")
print(f"Crédito solicitado al fabricante: ${credito_fabricante:}")
print(f"Intereses a pagar al fabricante: ${intereses_fabricante:}")
print(f"Total a pagar al fabricante: ${total_credito:}")