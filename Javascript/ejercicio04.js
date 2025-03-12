//4. Hacer un algoritmo en Pseint que lea tres números enteros y los muestre de menor a mayor.
let num01;
let num02;
let num03;
let Intercambio;


// Solicitar entrada al usuario

num01=parseInt(prompt("Ingrese el primer número:"));

num02=parseInt(prompt("Ingrese el segundo número:"));


num03=parseInt(prompt("Ingrese el segundo número:"));

if (num01 > num02){
Intercambio = num01;
num01 = num02;
num02 = Intercambio;
}

if (num02 > num03) {
Intercambio = num02;
num02 = num03;
num03 = Intercambio;
}

if (num01 > num02) {
Intercambio = num01;
num01 = num02;
num02 = Intercambio;
}

console.log("Los numeros ordenados son: ", num01, num02, num03);
alert("Los numeros ordenados son: " + num01 + "," +  num02 + "," + num03 );


/*

//4. Hacer un algoritmo en Pseint que lea tres números enteros y los muestre de menor a mayor.
Proceso Numeros_eNTEROS_mAYOR_mENOR 
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
	
	Si num01 > num02 Entonces
		Intercambio <- num01
		num01 <- num02
		num02 <- Intercambio
	FinSi
	
	Si num02 > num03 Entonces
		Intercambio<- num02
		num02 <- num03
		num03 <- Intercambio
	FinSi
	
	Si num01 > num02 Entonces
		Intercambio <- num01
		num01 <- num02
		num02 <- Intercambio
	FinSi
	
	Escribir "Los numeros ordenados son:" "," num01, "," num02, "," num03
	
FinProceso*/
