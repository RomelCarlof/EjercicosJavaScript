# Proceso resto_cociente 

primero = input("Ingrese un valor de A:")
segundo = input("Ingrese un valor de B:")

try:
    A = int(primero)
    B = int(segundo)
    


    if B == 0:
        print("No se puede dividir por cero.")
    else:
        cociente = 0

        while A >= B:
            A = A - B
            cociente = cociente + 1
        #Fin Mientras
    
        print("El cociente es:", cociente)
        print("El resto es:", A)
    
except ValueError:   
    print("Por favor, ingrese solo valores numéricos.")