
nota1 = float(input("Ingrese la primera nota:"))

nota2 = float(input("Ingrese la segunda nota:"))

nota3 = float(input("Ingrese la tercera nota:"))

#cálculo del promedio Final

PromedioFinal = (nota1 + nota2 + nota3) / 3

if PromedioFinal <= 10:

    print( "Promedio" , PromedioFinal)
    print(" El alumno ha desaprobado")



else :
    
    print(f"Promedio: {PromedioFinal:.2f}")
    print("El alumno ha aprobado")
  

