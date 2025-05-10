// Proceso resto_cociente 
let cociente;

let A = parseInt(prompt("Ingrese un valor de A:"));
let B = parseInt(prompt("Ingrese un valor de B:"));

if (isNaN(A) || isNaN(B)) {
    alert("Por favor, ingrese solo valores numéricos.");
} else if (B === 0) {
    alert("No se puede dividir por cero.");
} else {
    cociente = 0;

    while (A >= B) {
        A = A - B;
        cociente = cociente + 1;
    } // Fin Mientras
    
    console.log("El cociente es: ", cociente);
    alert("El resto es: " + A);
}
