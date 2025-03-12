let nota1;
let nota2;
let nota3;

nota1 = parseFloat(prompt("Ingrese la primera nota:"));
nota2 = parseFloat(prompt("Ingrese la segunda nota:"));
nota3 = parseFloat(prompt("Ingrese la tercera nota:"));

// Verificar si las entradas son válidas
if (isNaN(nota1) || isNaN(nota2) || isNaN(nota3)) {
    console.log("Error: Ingrese valores numéricos válidos.");
} else if (nota1 < 0 || nota1 > 20 || nota2 < 0 || nota2 > 20 || nota3 < 0 || nota3 > 20) {
    console.log("Error: Las notas deben estar entre 0 y 20.");
} else {

    //cálculo del promedio Final

    let PromedioFinal = (nota1 + nota2 + nota3) / 3

    if (PromedioFinal <= 10) {
        console.log(`Promedio: ${PromedioFinal.toFixed(2)}`);
        console.log("El alumno ha desaprobado");
        alert("El alumno ha desaprobado");
        alert(`Promedio: ${PromedioFinal.toFixed(2)}`);

    } else {
        console.log(`Promedio: ${PromedioFinal.toFixed(2)}`);
        console.log("El alumno ha aprobado")
        alert("El alumno ha aprobado")
        alert(`Promedio: ${PromedioFinal.toFixed(2)}`);
    }
}



/*
//Hacer un algoritmo en Pseint para calcular el promedio de tres notas y determinar si el estudiante aprobó o no.
Algoritmo Promedio_Notas
	
    Definir nota1, nota2, nota3, PromedioFinal Como Real
	
    Escribir "Ingrese la primera nota:"
    Leer nota1
	
    Escribir " Ingrese la segunda nota:"
    Leer nota2
	
    Escribir "Ingrese la tercera nota:"
    Leer nota3
	

    //cálculo del promedio Final
	
    PromedioFinal <- (nota1+nota2+nota3)/3
	
    Si PromedioFinal <= 10 Entonces
        Escribir "Promedio", PromedioFinal 
        Escribir "El alumno ha desaprobado:"
    	
    SiNo
        Escribir "Promedio", PromedioFinal
        Escribir "El alumno ha aprobado"

    FinSi

FinAlgoritmo */
