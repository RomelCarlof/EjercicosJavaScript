#Algoritmo pago_empleado_heladeria

#Solicitar y validar el número identificador del empleado (debe ser 1 a 4)
try:
    print("Ingrese el número identificador del empleado:")
    print("1 - Cajero ($56/día)")
    print("2 - Servidor ($64/día)")
    print("3 - Preparador de mezclas ($80/día)")
    print("4 - Mantenimiento ($48/día)")

    id = int(input("Ingrese el número identificador del empleado (1 a 4): "))

    if id < 1 or id > 4:
        print("Número de empleado inválido. Por favor, ingrese un número entre 1 y 4.")
    else:
        print(f"Empleado seleccionado con ID {id}.")
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")



# Solicitar y validar la cantidad de días trabajados (máximo 6)
try:
    dias = int(input("Ingrese la cantidad de días trabajados en la semana (máximo 6): "))
    if dias < 1 or dias > 6:
        print("La cantidad de días ingresada es inválida. Debe estar entre 1 y 6.")
    else:
        print(f"Has ingresado {dias} día(s) válidos.")
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")



# Asignar el salario diario según el identificador del empleado (# Simulación de un switch con un diccionario)
tarifas = {1: 56, 2: 64, 3: 80, 4: 48}
salario = tarifas.get(id, 0)

if salario == 0:
    print("ID de empleado no válido.")

# Calcular el total a pagar
total = salario * dias

# Mostrar el resultado
print(f"El pago total al empleado es: ${total}")


#Fin del algoritmo
