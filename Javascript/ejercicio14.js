//Algoritmo NumeroPrimo

let num;
let i;
let contador = 0;

// Pedir al usuario un número
num = parseInt(prompt("Ingresa un número entero positivo (1..10):"));

// Validar que el número esté en el rango de 1 a 10
while (num < 1 || num > 10) {
    console.log("El número está fuera del rango 1..10.");

    num = parseInt(prompt("Ingresa un número nuevamente:"));

}


// Caso especial: si el número es menor que 2, no es primo

if (num < 2) {

    console.log("El número NO es primo.")
    alert("El número NO es primo.")
} else {



    // Repetir
    //     Si (num = 0) Entonces
    //         Escribir "El número NO es correcto"
    //         Escribir "Ingresa un número nuevamente:"
    //         Leer num
    //     FinSi
    // Hasta Que num <> 0



    // Iniciar contador de divisores


    // Probar divisiones desde 1 hasta el número
    // Probar divisiones desde 1 hasta el número
    for (let i = 1; i <= num; i++) {

        // Verificar si 'i' es un divisor de 'num'
        if (num % i === 0) {
            // Incrementar el contador de divisores
            contador = contador + 1;
            // Mostrar el divisor encontrado
            console.log("Divisor encontrado:", i);
        }
    }



    // Determinar si es primo
    if (contador === 2) {
        console.log("El número ES primo.");
    } else {
        console.log("El número NO es primo.");
        alert("El número NO es primo.")

    }
}
