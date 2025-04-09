# Declarar variables
"""let numero;"""
negativo = 0; 	# Inicializar la variable negativo

#  Solicitar entrada al usuario
numero= int(input("Ingrese un número"))

# Evaluar si el número es negativo

if numero < 0:
		negativo = 1  #Marcar que el número es negativo


# Mostrar resultados al usuario
if negativo == 1:
       
        print("El número ingresado es negativo");
else: 
        
        print("El número ingresado no es negativo")





"""/*//Hacer un algoritmo en Pseint que lea un número entero por el teclado y determinar si es negativo.

Proceso Entero_Positivo_Negativo
	
	// Declarar variables
	Definir numero Como Entero
		Definir negativo Como Entero
		
	// Inicializar la variable negativo
	negativo <- 0  
	
	// Solicitar entrada al usuario
	Escribir "Ingrese un número:"
	Leer numero  // Leer el número ingresado por el usuario
	
	// Evaluar si el número es negativo
	Si numero < 0 Entonces
		negativo <- 1  // Marcar que el número es negativo
	FinSi
	
	// Mostrar resultados al usuario
	Si negativo = 1 Entonces
		Escribir "El número ingresado es negativo"
	SiNo
		Escribir "El número ingresado es positivo"
	FinSi
	
FinProceso*/"""
