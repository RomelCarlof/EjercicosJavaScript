#Algoritmo ContadorPara


entrada = input("Ingrese un número entero: ")

try:
    n = int(entrada) 
    print("¡No ingresaste un número válido!")

    if n < 0:
        print("El factorial no está definido para números negativos.")
    
    else:
        factorial = 1;  # 'factorial' es un número entero
        for  i in range(1,n+1):
            factorial *= i # Multiplicación de enteros
    #FinPara
        print(f"El factorial de {n} es {factorial}")
except ValueError:
    print("¡No ingresaste un número válido!")
#FinAlgoritmoS