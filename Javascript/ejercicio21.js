//Algoritmo ContadorPara
let n;
let factorial;

n = prompt("Ingrese un número entero: ");
n = parseInt(n); // Lo conviertes a número

if (isNaN(n)) {
    alert("¡No ingresaste un número válido!");

}else if (n < 0) {
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