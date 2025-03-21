let letra;
do {
    letra = prompt("Ingrese una letra: ").trim(); // Eliminar espacios en blanco
    
    //// Validar que solo ingrese una letra y no otro carácter

    if (letra.length !== 1 || !isNaN(letra)) {
        alert("Por favorm, ingrese  solo una letra.");
    }

} while (letra.length !== 1 || !isNaN(letra));


// Convertir a minúscula para simplificar la comparación
letra = letra.toLowerCase();

if (letra === "a" || letra === "e" || letra === "i" || letra === "o" || letra === "u") {
    console.log("La letra es un vocal");
    alert("La letra es un vocal");
} else {

    console.log("La letra no es un vocal");
    alert("La letra no es un vocal");
}




















/*lgoritmo Numero_MayoR_mENOR
    //Definir variables
    Definir letra Como Caracter
	
    Escribir "Ingrese un letra:"
    Leer letra
	
    Si (letra = "a") O (letra = "A") O (letra = "e") O (letra = "E") O (letra = "i") O (letra = "I") O (letra = "o")O  (letra = "O") O ( letra = "u") O ( letra = "U")Entonces
        Escribir "La letra es un vocal"
    SiNo
    	
    Escribir "La letra no es una vocal"
FinSi
FinProceso*/
