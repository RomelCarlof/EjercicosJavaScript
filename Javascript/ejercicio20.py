#Algoritmo operaciones_enteros


    #Leer 4 números enteros positivos
    num1 = Escribir "Ingrese el primer número entero positivo:"
    Leer num1
    Escribir "Ingrese el segundo número entero positivo:"
    Leer num2
    Escribir "Ingrese el tercer número entero positivo:"
    Leer num3
    Escribir "Ingrese el cuarto número entero positivo:"
    Leer num4
	
    // 1. ¿Cuántos números son pares?
    parCount <- 0
    Si num1 MOD 2 = 0 Entonces
        parCount <- parCount + 1
	FinSi
	
	Si num2 MOD 2 = 0 Entonces
		parCount <- parCount + 1
	FinSi

	Si num3 MOD 2 = 0 Entonces
		parCount <- parCount + 1
	Finsi

	Si num4 MOD 2 = 0 Entonces
		parCount <- parCount + 1
	FinSi

	
 
    Escribir "La cantidad de números pares es: ", parCount
	
    // 2. ¿Cuál es el mayor de todos?
    mayor1 <- num1
    Si num2 > mayor1 Entonces
        mayor1 <- num2
	Finsi

	Si num3 > mayor1 Entonces
		mayor1 <- num3
	Finsi
	
	Si num4 > mayor1 Entonces
		mayor1 <- num4
	Finsi
	
	Escribir "El mayor número es: ", mayor1
	
    // 3. Si el tercero es par, calcular el cuadrado del segundo.
    Si num3 MOD 2 = 0 Entonces
        cuadrado <- num2 * num2
        Escribir "El cuadrado del segundo número es: ", cuadrado
    FinSi
	
    // 4. Si el primero es menor que el cuarto, calcular la media de los 4 números.
    Si num1 < num4 Entonces
        media <- (num1 + num2 + num3 + num4) / 4
        Escribir "La media de los 4 números es: ", media
    FinSi
	
    // 5. Si el segundo es mayor que el tercero, verificar si el tercero está comprendido entre 50 y 700.
    //    Si se cumple, calcular la suma de los 4 números.
    Si num2 > num3 Entonces
        Si num3 >= 50 Y num3 <= 700 Entonces
            suma <- num1 + num2 + num3 + num4
            Escribir "La suma de los 4 números es: ", suma
        FinSi
    FinSi
FinAlgoritmo