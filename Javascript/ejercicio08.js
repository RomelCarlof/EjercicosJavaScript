let nota1;
let nota2;
let nota3;

nota1 = parseFloat(prompt("Ingrese la primera nota:"));

nota2 = parseFloat(prompt("Ingrese la segunda nota:"));

nota3 = parseFloat(prompt("Ingrese la tercera nota:"));

//cálculo del promedio Final

let PromedioFinal = (nota1 + nota2 + nota3) / 3;

if (PromedioFinal <= 10) {

    console.log( "Promedio"  +  PromedioFinal);
    alert( "Promedio"  +  PromedioFinal);

    console.log(" El alumno ha desaprobado");
    alert("El alumno ha desaprobado");


} else {

    console.log("Promedio"  +  PromedioFinal.toFixed(2));
    alert("Promedio"  +  PromedioFinal.toFixed(2));

    console.log("El alumno ha aprobado");
    alert("El alumno ha aprobado")

}


/*

/Hacer un algoritmo en Pseint para calcular el promedio de tres notas y determinar si el estudiante aprobó o no.
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

FinSi*/
