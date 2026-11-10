numero = int(input("Introduce un número de tres cifras: "))

centenas = numero // 100
decenas = (numero // 10) % 10
unidades = numero % 10

suma = centenas + decenas + unidades

print("Centenas:", centenas)
print("Decenas:", decenas)
print("Unidades:", unidades)
print("Suma de las cifras:", suma)
print("Número invertido:",unidades.decenas,centenas)