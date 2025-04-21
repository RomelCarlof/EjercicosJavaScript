
//Algoritmo Calcular_Precio
let cantidad;
let precio;
let total;

// Solicitar la cantidad de CDs a comprar
cantidad = parseInt(prompt("Ingrese la cantidad de CDs vírgenes que desea comprar:"))

// Determinar el precio unitario según la cantidad
if (cantidad <= 9) {
    precio = 10;
} else if (cantidad >= 10 || cantidad <= 99) {
    precio = 8;
} else if (cantidad >= 100 || cantidad <= 499) {
    precio = 7;
} else {
    // Para cantidades de 500 o más 
    precio = 6;
}
// Calcular el total a pagar 
total = cantidad * precio;
// Mostrar resultados
console.log("El precio unitario es: $", precio);
alert("El precio unitario es: $" + precio);
console.log("El total a pagar es: $", total);
alert("El total a pagar es: $"+ total);
//FinAlgoritmo


/*//La ganancia para el vendedor es de 8, 25 % de la venta.Realizar un algoritmo en Pseint que dado un número de CDs a vender calcule el precio total para el cliente y la ganancia para el vendedor.
// Algoritmo Calcular_Precio_Ganancia
    let cantidad;
    let precio; 
    let total; 
    Definir ganancia Como Real
        // Solicitar la cantidad de CDs a comprar
        Escribir "Ingrese la cantidad de CDs vírgenes que desea comprar:"
        Leer cantidad
// Determinar el precio unitario según la cantidad
	Si cantidad <= 9 Entonces
precio < -10
Sino
		Si cantidad >= 10 y cantidad <= 99 Entonces
precio < - 8
Sino
			Si cantidad >= 100 y cantidad <= 499 Entonces
precio < - 7
Sino
// Para cantidades de 500 o más 
precio < - 6
Finsi
Finsi
Finsi
// Calcular el total a pagar 
total < - cantidad * precio
ganancia < - precio * 0.0825
// Mostrar resultados
 Escribir "El precio unitario es: $", precio 
 Escribir "El total a pagar es: $", total
Escribir "La ganancia para el vendedor es: $", ganancia

FinAlgoritmo*/
