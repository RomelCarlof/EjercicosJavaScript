# Algoritmo operaciones_enteros

# Leer 4 números enteros positivos
num1 = int(input("Ingrese el primer número entero positivo: "))
num2 = int(input("Ingrese el segundo número entero positivo: "))
num3 = int(input("Ingrese el tercer número entero positivo: "))
num4 = int(input("Ingrese el cuarto número entero positivo: "))

# 1. ¿Cuántos números son pares?
parCount = 0

if num1 % 2 == 0:
    parCount = parCount + 1

if num2 % 2 == 0:
    parCount = parCount + 1

if num3 % 2 == 0:
    parCount = parCount + 1

if num4 % 2 == 0:
    parCount = parCount + 1

print("La cantidad de números pares es:", parCount)

# 2. ¿Cuál es el mayor de todos?
mayor1 = num1

if num2 > mayor1:
    mayor1 = num2

if num3 > mayor1:
    mayor1 = num3

if num4 > mayor1:
    mayor1 = num4

print("El mayor número es:", mayor1)

# 3. Si el tercero es par, calcular el cuadrado del segundo.
if num3 % 2 == 0:
    cuadrado = num2 * num2
    print("El cuadrado del segundo número es:", cuadrado)

# 4. Si el primero es menor que el cuarto, calcular la media de los 4 números.
if num1 < num4:
    media = (num1 + num2 + num3 + num4) / 4
    print("La media de los 4 números es:", media)

# 5. Si el segundo es mayor que el tercero, verificar si el tercero está comprendido entre 50 y 700.
# Si se cumple, calcular la suma de los 4 números.
if num2 > num3:
    if 50 <= num3 <= 700:
        suma = num1 + num2 + num3 + num4
        print("La suma de los 4 números es:", suma)
