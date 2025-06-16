#2. Escribe una función que reciba números como entrada y devuelva la suma de los mismos. La función debe ser capaz de recibir una cantidad indeterminada de números. La función
 # no debe recibir directamente ningún objeto complejo (lista, conjunto, etc.).

def sumar (*numeros):
    sumar = 0
    for numero in numeros:
        sumar += numero
    return sumar

print(sumar(1,2,3,4,5,6,10,11,12,14,16))

