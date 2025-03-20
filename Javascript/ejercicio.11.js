let num01;
let num02;
let num03;


num01 = parseFloat(prompt("Ingrese el primer número:"));
num02 = parseFloat(prompt("Ingrese el segundo número:"));
num03 = parseFloat(prompt("Ingrese el tercer número:"));

// Ordenamiento en orden descendente (mayor a menor)
if (num01 < num02) {
    let temp = num01;
    num01 = num02;
    num02 = temp;
}

if (num02 < num03) {
    let temp = num02;
    num02 = num03;
    num03 = temp;
}

if (num01 < num02) {
    let temp = num01;
    num01 = num02;
    num02 = temp;
}

// Mostrar el resultado correctamente separado
alert("Los numeros ordenados son:" + num01 + "," + num02 + ","  + num03);
console.log("Los numeros ordenados son:" + num01 + "," + num02 + "," + num03);

/*
Algoritmo Numero_MayoR_mENOR
	
        Definir num01 Como Entero
        Definir num02 Como Entero
        Definir num03 Como Entero
        Definir Intercambio Como Entero
    	
        Escribir "Ingrese el primer número:"
        Leer num01
    	
        Escribir "Ingrese el segundo número:"
        Leer num02
    	
        Escribir "Ingrese el tercer número:"
        Leer num03
    	
        Si num01 < num02 Entonces
            Intercambio <- num01
            num01 <- num02
            num02 <- Intercambio
        FinSi
    	
        Si num02 < num03 Entonces
            Intercambio<- num02
            num02 <- num03
            num03 <- Intercambio
        FinSi
    	
        Si num01 < num02 Entonces
            Intercambio <- num01
            num01 <- num02
            num02 <- Intercambio
        FinSi
    	
        Escribir "Los numeros ordenados son:" "," num01, "," num02, "," num03

	
FinProceso
 */
