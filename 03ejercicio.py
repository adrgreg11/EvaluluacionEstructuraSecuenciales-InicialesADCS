segundos = int(input("Tiempo en segundos: "))

dias = segundos // 86400
resto = segundos % 86400

horas = resto // 3600
resto = resto % 3600

minutos = resto // 60
segundos_finales = resto % 60

print(segundos, "segundos son", dias, "días,", horas, "horas,", minutos, "minutos y", segundos_finales, "segundos.")