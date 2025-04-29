//Algoritmo ContadorPara
let n;
let suma;
let i;

n = prompt("Ingrese un número entero: ");
n = parseInt(n);
if (isNaN(n)) {
    console.log("¡No ingresaste un número válido!");
    alert("¡No ingresaste un número válido!");
} else if (n < 0) {
    console.log("La suma no está definida para números negativos.");
    alert("La suma no está definida para números negativos.");
} else {
    suma = 0;  // Inicia el número entero
    for (let i = 1; i <= n; i++) {
        suma = suma + i  // Sumar  enteros
    }//FinPara
    console.log("El factorial de ", n, " es ", suma);
    alert("El factorial de" + n + "es ", +suma);
}//FinSi
//FinAlgoritmo