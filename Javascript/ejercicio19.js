//Algoritmo pago_empleado_heladeria
let id;
let dias;
let salario;
let total;

// Solicitar y validar el número identificador del empleado (debe ser 1 a 4)
do {
    console.log("Ingrese el número identificador del empleado:");
    alert("Ingrese el número identificador del empleado:");
    console.log("1 - Cajero ($56/día)");
    alert("1 - Cajero ($56/día)");
    console.log("2 - Servidor ($64/día)");
    alert("2 - Servidor ($64/día)");
    console.log("3 - Preparador de mezclas ($80/día)");
    alert("3 - Preparador de mezclas ($80/día)");
    console.log("4 - Mantenimiento ($48/día)");
    alert("4 - Mantenimiento ($48/día)");
    id = parseInt(prompt("Ingrese el número identificador del empleado (1 a 4):"));

    if (id < 1 || id > 4) {
        console.log("Número de empleado inválido. Por favor, ingrese un número entre 1 y 4.");
        alert("Número de empleado inválido. Por favor, ingrese un número entre 1 y 4.");
    }
} while (id < 1 || id > 4);

// Solicitar y validar la cantidad de días trabajados (máximo 6)
do {
    dias = parseInt(prompt("Ingrese la cantidad de días trabajados en la semana (máximo 6):"));
    if (dias < 1 || dias > 6) {
        console.log("La cantidad de días ingresada es inválida. Debe estar entre 1 y 6.");
        alert("La cantidad de días ingresada es inválida. Debe estar entre 1 y 6.");
    }
} while (dias < 1 || dias > 6);

// Asignar el salario diario según el identificador del empleado
switch (id) {
    case 1:
        salario = 56;
        break;
    case 2:
        salario = 64;
        break;
    case 3:
        salario = 80;
        break;
    case 4:
        salario = 48;
        break;
    default:
        salario = 0;
        alert("ID de empleado no válido.");
        break;
}

// Calcular el total a pagar
total = salario * dias;

// Mostrar el resultado
console.log("El pago total al empleado es: $" + total);
alert("El pago total al empleado es: $" + total);

//Fin del algoritmo
