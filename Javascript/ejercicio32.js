//32. Se quiere saber cuál es la ciudad con la población de más personas, son tres provincias y once ciudades, hacer un algoritmo en Pseint que nos permita saber eso. (NO HAY DATOS SUFICIENTES)
//Proceso CiudadMayorPoblacion
    let provincias;
    let ciudades;
    let i, j;
    let ciudadMayor;
    let nombreCiudad;
    let  poblacionMayor, poblacionActual;
    
    provincias = 3;
    ciudades = 11;
    poblacionMayor = 0;
    ciudadMayor = ""
	
    for (i = 1; i<=provincias, i++)
        Escribir "Provincia ", i, ":"
        Para j <- 1 Hasta ciudades Hacer
            Escribir "Ingrese el nombre de la ciudad ", j, ": "
            Leer nombreCiudad
            Escribir "Ingrese la población de ", nombreCiudad, ": "
            Leer poblacionActual
			
            Si poblacionActual > poblacionMayor Entonces
                poblacionMayor <- poblacionActual
                ciudadMayor <- nombreCiudad
            FinSi
        Fin Para
    Fin Para
	
    Escribir "La ciudad con mayor población es: ", ciudadMayor, " con ", poblacionMayor, " habitantes."
FinProceso