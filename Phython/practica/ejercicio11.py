

num01 = int(input("Ingrese el primer número:"))
num02 = int(input("Ingrese el segundo número:"))
num03 = int(input("Ingrese el tercer número:"))

# Ordenamiento en orden descendente (mayor a menor)
if num01 < num02: 
    temp = num01
    num01 = num02
    num02 = temp


if num02 < num03:
    temp = num02
    num02 = num03
    num03 = temp

if num01 < num02:
    temp = num01
    num01 = num02
    num02 = temp


# Mostrar el resultado correctamente separado
print("Los numeros ordenados son:" , num01 , "," , num02 , ","  , num03)
