//4. Hacer un algoritmo en Pseint que lea tres números enteros y los muestre de menor a mayor.
"""let num01;
let num02;
let num03;
let Intercambio;"""


# Solicitar entrada al usuario

num01=int(input("Ingrese el primer número:"))

num02=int(input("Ingrese el segundo número:"))


num03=int(input("Ingrese el segundo número:"))

if num01 > num02:
    Intercambio = num01
    num01 = num02
    num02 = Intercambio


if num02 > num03:
    Intercambio = num02
    num02 = num03
    num03 = Intercambio


if num01 > num02:
    Intercambio = num01
    num01 = num02
    num02 = Intercambio

print("Los numeros ordenados son: " + num01 + "," +  num02 + "," + num03 );