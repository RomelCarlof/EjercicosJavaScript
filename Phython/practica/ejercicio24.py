#Algoritmo SumaParesMientras
#let n;
#let suma;
#let i;
entrada = input("Ingrese un número entero positivo: ")
suma = 0
i = 2

try:
    # Se establece el límite como 1000
    while i <= 1000:
        suma = suma + i
        i = i + 2

    print("La suma de los números pares menores o iguales a 1000 es:", suma)

except ValueError:
    print("¡No ingresaste un número válido!")