
#Algoritmo Calcular_Precio


#Solicitar la cantidad de CDs a comprar
cantidad =  int(input("Ingrese la cantidad de CDs vírgenes que desea comprar:"))

# Determinar el precio unitario según la cantidad
if cantidad <= 9 :
    precio = 10
elif cantidad >= 10 or cantidad <= 99:
    precio = 8
elif cantidad >= 100 or cantidad <= 499:
    precio = 7
else: 
# Para cantidades de 500 o más 
    precio = 6

# Calcular el total a pagar 
total = cantidad * precio
#Mostrar resultados
print("El precio unitario es: $", precio)
print("El total a pagar es: $", total)

