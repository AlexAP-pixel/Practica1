from datetime import datetime

fecha_nacimiento = "18/1/2002"

# Convertir la fecha de nacimiento a un objeto de fecha
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

fecha = "8/3/2023"

# Convertir la fecha de nacimiento a un objeto de fecha
fecha = datetime.strptime(fecha, "%d/%m/%Y")

# Calcular la diferencia entre la fecha actual y la fecha de nacimiento en días
diferencia = fecha - fecha_nacimiento
dias_vividos = diferencia.days

# Imprimir el resultado
print("Has vivido", dias_vividos, "días hasta el 8 de marzo de 2023.")
resultado = dias_vividos % 3
print("Tu numero es", resultado)