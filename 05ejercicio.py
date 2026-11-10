importe = float(input("Importe de la compra (€): "))
entregado = float(input("Dinero entregado (€): "))

cambio = round((entregado - importe) * 100)

print("Cambio:", cambio / 100, "€")

billetes_20 = cambio // 2000
cambio = cambio % 2000