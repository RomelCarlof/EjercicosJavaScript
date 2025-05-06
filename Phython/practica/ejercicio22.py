#Algoritmo ContadorPara

entrada = input("Ingrese un número entero: ")

try:

    n = int(entrada)
    print("¡No ingresaste un número válido!")

    if n < 0:
        print("La suma no está definida para números negativos.")

    else:
        suma = 0 # Inicia el número entero
        for i in range(1, n+1):
         suma = suma + i  #Sumar  
    #FinPara
        print(f"El factorial de {n} es {suma}")

except ValueError:
    print("¡No ingresaste un número válido!")

