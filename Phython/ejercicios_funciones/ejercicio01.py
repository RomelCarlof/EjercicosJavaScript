#1. Escribe una función que reciba como entrada una lista con números y devuelva como resultado una lista con los cuadrados de los números contenidos en la lista de entrada.

def Obtener_Cuadrados(numeros):
    Resultado = []

    for numero in numeros :
        Resultado.append(numero ** 2)
    return Resultado

    print(Obtener_Cuadrados([1,2,3,4,5,6,7,8,9]))



