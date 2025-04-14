#/Algoritmo Convertidor_Pulgadas_Kilogramo

CentimetroCant= float( input("Ingrese una cantidad en Centímetros:"))
   
    
LibrasCant =float( input("Ingrese una cantidad en Libras:"))

    
# Calcular conversiones
TotPulgadas = CentimetroCant / 2.54
TotKilo = LibrasCant * 0.453592
    
#Mostrar resultados
print( f"TOTAL DE CÁLCULO EN PULGADAS:  {TotPulgadas:.2f}")
  
print( f"TOTAL DE CÁLCULO EN KILOGRAMOS: {TotKilo:.2f}")
  
