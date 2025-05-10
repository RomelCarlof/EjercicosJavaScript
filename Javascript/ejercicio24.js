//Algoritmo SumaParesMientras
let n;
let suma;
let i;
n = prompt("Ingrese un número entero positivo: ");
n = parseInt(n);

suma = 0;
i = 2;

if (isNaN(n)) {
    console.log("¡No ingresaste un número válido!");
    alert("¡No ingresaste un número válido!");
} else if (n < 0) {
    console.log("La suma no está definida para números negativos.");
    alert("La suma no está definida para números negativos.");
} else {
    while (i <= 1000) {
        suma =suma + i;
        i = i + 2;
    }//Fin Mientras
        console.log("La suma de los números pares menores o iguales a ", 1000, " es: ", suma);
        alert("La suma de los números pares menores o iguales a "+ 1000 + " es: " + suma);
} //FinProceso	