//Algoritmo ContadorPara
let n;
let factorial;
let i;

n = parseInt(prompt("Ingrese un número entero: "));


if (n < 0) {
    console.log("El factorial no está definido para números negativos.");
    alert("El factorial no está definido para números negativos.");
} else {
    factorial = 1;  // 'factorial' es un número entero
    for (let i = 1; i <= n; i++) {
        factorial = factorial * i ; // Multiplicación de enteros
    }//FinPara
    console.log("El factorial de ", n, " es ", factorial);
    alert("El factorial de ", + n + " es " +factorial);
}
//FinAlgoritmoS