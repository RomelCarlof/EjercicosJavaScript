let num01;
let num02;

num01 = parseFloat(prompt("Ingrese el primer número:"));
num02 = parseFloat(prompt("Ingrese el segundo número:"));


if (num01 < num02) {
    let Intercambio = num01;
    num01 = num02;
    num02 = Intercambio;
}


// Mostrar el resultado ordenado (mayor a menor)
console.log("Los numeros ordenados son:" + num01 + "," + num02);
alert("Los números ordenados son: " + num01 + ", " + num02);








/*11. Hacer un algoritmo en Pseint que lea tres números y diga cuál es el mayor.

Algoritmo Numero_MayoR_mENOR
	
        Definir num01 Como Entero
        Definir num02 Como Entero
        Definir Intercambio Como Entero
    	
        Escribir "Ingrese el primer número:"
        Leer num01
    	
        Escribir "Ingrese el segundo número:"
        Leer num02
    	
	
        Si num01 < num02 Entonces
            Intercambio <- num01
            num01 <- num02
            num02 <- Intercambio
        FinSi
    	
    	
        Escribir "Los numeros ordenados son:" "," num01, "," num02 */
