//32. Se quiere saber cuál es la ciudad con la población de más personas, son tres provincias y once ciudades, hacer un algoritmo en Pseint que nos permita saber eso. (NO HAY DATOS SUFICIENTES)
//Proceso CiudadMayorPoblacion
    let provincias;
    let ciudades;
    let i, j;
    let ciudadMayor;
    let nombreCiudad;
    let  poblacionMayor, poblacionActual;
    let provinciaMayor = 0;
    
    provincias = 3;
    ciudades = 11;
    poblacionMayor = 0;
    ciudadMayor = "";

	
  
    for (i = 1; i <= provincias; i++) {
    console.log("Provincia " + i);

        for ( j = 1;  j<= ciudades; j++){
            nombreCiudad = prompt("Ingrese el nombre de la ciudad " + j +  " de la provincia " + i + ": ");
            poblacionActual = parseInt(prompt("Ingrese la población de " + nombreCiudad + ": "), 10);
            
            if (poblacionActual > poblacionMayor){
                poblacionMayor = poblacionActual;
                ciudadMayor = nombreCiudad;
                provinciaMayor = i; // guardamos la provincia también
            } 
        }
    }
    console.log("---------------------------------------------");
    console.log("La ciudad con mayor población es: " + ciudadMayor + " con " + poblacionMayor +  " habitantes(Provincia " + provinciaMayor + ").");
    alert("La ciudad con mayor población es: " + ciudadMayor + " con " + poblacionMayor + " habitantes(Provincia " + provinciaMayor + ").");