

num01 = int(input("Ingrese el primer número:"))
num02 = int(input("Ingrese el segundo número:"))


if num01 < num02:
    Intercambio = num01
    num01 = num02
    num02 = Intercambio



# Mostrar el resultado ordenado (mayor a menor)
print("Los numeros ordenados son:" , num01  , num02)
