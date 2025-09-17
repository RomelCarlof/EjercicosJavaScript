// 32. Se quiere saber cuál es la ciudad con mayor población
//    Hay 3 provincias y 11 ciudades
//    Algoritmo en JavaScript

let provincias, ciudades;
let i, j;
let ciudadMayor, nombreCiudad;
let poblacionMayor, poblacionActual;
let provinciaMayor;

provincias = 3;
ciudades = 11;
poblacionMayor = 0;
ciudadMayor = "";
provinciaMayor = 0;

for (i = 1; i <= provincias; i++) {
    console.log("Provincia " + i);

    for (j = 1; j <= ciudades; j++) {
        nombreCiudad = prompt("Ingrese el nombre de la ciudad " + j + " de la provincia " + i + ": ");
        poblacionActual = parseInt(prompt("Ingrese la población de " + nombreCiudad + ": "), 10);

        if (poblacionActual > poblacionMayor) {
            poblacionMayor = poblacionActual;
            ciudadMayor = nombreCiudad;
            provinciaMayor = i; // guardamos la provincia también
        }
    }
}

console.log("---------------------------------------------");
console.log("La ciudad con mayor población es: " + ciudadMayor + 
            " con " + poblacionMayor + " habitantes (Provincia " + provinciaMayor + ").");

alert("La ciudad con mayor población es: " + ciudadMayor + 
      " con " + poblacionMayor + " habitantes (Provincia " + provinciaMayor + ").");
