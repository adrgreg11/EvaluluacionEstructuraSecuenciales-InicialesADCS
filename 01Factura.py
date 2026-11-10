#Factura con IVA

precio = float(input("Introduce el precio sin IVA: "))

iva = precio * 0.21
precio_final = precio + iva

print("IVA (21%):", iva)
print("Precio final:", precio_final)

