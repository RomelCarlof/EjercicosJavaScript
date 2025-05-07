let n;
let numero;
let i;

n = prompt("Ingrese un número entero positivo");
n = parseInt(n);

if (isNaN(n) || n <= 0) {
    console.log("¡No ingresaste un número válido!");
    alert("¡No ingresaste un número válido!");
} else {
    let Suma = 0;
    for (let i = 1; i <= n; i += 2) {
        Suma += i;
    }//FinPara
    console.log("La suma de los números enteros impares menores o iguales a " + n + " es:  " + Suma);
    alert("La suma de los números enteros impares menores o iguales a " + n + " es:  " + Suma);
}//FinAlgoritmo