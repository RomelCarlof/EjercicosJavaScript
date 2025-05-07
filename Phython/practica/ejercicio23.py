

entrada = input("Ingrese un número entero positivo")

try:

    n = int(entrada)
    print("¡No ingresaste un número válido!")

    if n < 0:
        print("¡No ingresaste un número positivo!")

    else:
        Suma = 0
        for i in range(1, n + 1):
            Suma += i
    #FinPara
    print("La suma de los números enteros impares menores o iguales a " , n , " es:  " + Suma);
    
except ValueError:
    print("¡No ingresaste un número válido!")
#FinAlgoritmo