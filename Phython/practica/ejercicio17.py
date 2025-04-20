#Algoritmo CalcularHora


# Pedir al usuario que ingrese la hora actual
horas = int(input("Ingrrese la hora (0-23):"))

minutos = int(input("Ingrrese los minutos (0-59):"))

segundoss = int(input("Ingrrese los segundos (0-59):"))

# Sumar en segundos 
segundoss = segundoss + 1

# Si los segundos llegan a 60, reiniciar y sumar un minuto
if segundoss == 60:
    segundoss = 0
    minutos = minutos + 1

# Si los  minutos llegan a 60, reiniciar y sumar una hora
if minutos == 60:
    minutos = 0
    horas = horas + 1

#/Si las horas llegan a 24, reiniciar el día
if horas == 24:
    horas = 0


# Formatear con ceros a la izquierda

horaFormateada = str(horas).zfillt(2)
minutoFormateado = str(minutos).zfillt(2)
segundoFormateado = str(segundoss).zfillt(2)

# Mostrar la hora actualizada

print("La hora dentro de un segundo es: " + horas + ":" + minutos + ":" + segundoss)
