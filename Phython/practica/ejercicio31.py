#31. Hacer un algoritmo en Pseint parar calcular la media de los números pares e impares, sólo se ingresará diez números.
#Proceso Media123
   
Suma = 0;  # Se usa una variable para acumular la suma
Contador = 0;  # Se usa para contar los números sumados

for(  let i=0; i<= 10; i+=2){
        console.log("Escribir:",i);
        Suma = Suma + i
        Contador =Contador + 1  // Contamos los números sumados
    //Fin Para
    }
    Media = Suma / Contador  // Se calcula la media al final

    console.log("La media de los números pares de 10 números ingresados es: " + Media)
    alert("La media de los números pares de 10 números ingresados es: " + Media)
//FinProceso
