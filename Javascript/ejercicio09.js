let Paga;
let AumentoTotal;

Paga=parseFloat(prompt("Ingrese el Pago por mes:"));

//SUELDO POR MES
	// SEGUN EL TIPO DE PAGO
	if (Paga <= 2000){ 
		AumentoTotal= (Paga+(Paga*0.10));
		// Mostrar 
		console.log("Tipo de Paga con Aumento" + " " + AumentoTotal);
        alert("Tipo de Paga con Aumento" + " " + AumentoTotal);

    }else{ 
		AumentoTotal=(Paga+(Paga*0.05));
		// Mostrar 
		console.log(`Tipo de Paga con Aumento: ${AumentoTotal.toFixed(2)}`);  //Backticks (``) son útiles cuando necesitas incluir variables dentro de un string sin usar concatenación (+`).
        alert(`Tipo de Paga con Aumento: ${AumentoTotal.toFixed(2)}`);
		alert(`Tipo de Paga con Aumento: ${AumentoTotal.toFixed(2)}`);

	}
    /*Algoritmo Aumento_Personal
	// Variables
    // Variables
    Definir Paga, AumentoTotal Como Real
	
	Escribir "Ingrese el Pago por mes:"
	Leer Paga
	//////////modificacion 
	
	//SUELDO POR MES
	// SEGUN EL TIPO DE PAGO
	Si Paga <= 2000 Entonces
		AumentoTotal= (Paga+(Paga*0.10))
		// Mostrar 
		Escribir "Tipo de Paga con Aumento", " ", AumentoTotal
	SiNo
		AumentoTotal=(Paga+(Paga*0.05))
		// Mostrar 
		Escribir "Tipo de Paga con Aumento", " ", AumentoTotal
	FinSi
FinAlgoritmo */
