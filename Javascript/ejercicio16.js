//Algoritmo DiaDeLaSemana
// Definir numero Como Entero
let numero;
do {
	numero = parseInt(prompt("Ingrese un número del 1 al 7:").trim());

	if (numero === 1) {
		console.log("Lunes");
		alert("Lunes");
	} else if (numero === 2) {
		console.log("Martes");
		alert("Martes");
	} else if (numero === 3) {
		console.log("Miercoles");
		alert("Miercoles");
	} else if (numero === 4) {
		console.log("Jueves");
		alert("Jueves");
	} else if (numero === 5) {
		console.log("Viernes");
		alert("Viernes");
	} else if (numero === 6) {
		console.log("Sabado");
		alert("Sabado");
	} else if (numero === 7) {
		console.log("Domingo");
		alert("Domingo");
	} else {
		console.log("Número inválido. Intente nuevamente.");
		alert("Número inválido. Intente nuevamente.");
	}
} while (numero >= 1 || numero <= 7);