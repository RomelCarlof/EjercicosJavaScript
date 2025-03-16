let tipoMembresia;
let totalCompra;
let descuento = 0; // Inicializar en 0 para evitar errores
let totalConDescuento;


tipoMembresia = prompt("Ingrese el tipo de Menbresía (A,B,C):").toUpperCase();

totalCompra = parseFloat(prompt("Ingrese el total de la compra:"));


//PRIMER DESCUENTO
// SEGUN EL TIPO DE MENBRESÍA


if (isNaN(totalCompra) || totalCompra <= 0) {
    alert("Por favor, ingrese un valor válido para la compra.");
} else {

    switch (tipoMembresia) {

        case "A":
            descuento = totalCompra * 0.10;
            break;

        case "B":
            descuento = totalCompra * 0.15;
            break;

        case "C":

            descuento = totalCompra * 0.20;
            break;

        default:
            descuento = 0;
    }

    //calcular el total a pagar 

    totalConDescuento = totalCompra - descuento;

    // Mostrar 
    console.log("Tipo de Menbresía:" + tipoMembresia);
    alert("Tipo de Menbresía:" + tipoMembresia);

    console.log("Total de Compra:" + totalCompra.toFixed(2));
    alert("Total de Compra:" + totalCompra.toFixed(2));

    console.log("Descuento aplicado:" + descuento.toFixed(2));
    alert("Descuento aplicado:" + descuento.toFixed(2));

    console.log("Total con Descuento:" + totalConDescuento.toFixed(2));
    alert("Total con Descuento:" + totalConDescuento.toFixed(2));
}

/*
Algoritmo Tienda_Helado
    // Variables
    Definir tipoMembresia Como Caracter
    Definir totalCompra, descuento, totalConDescuento Como Real
	
    Escribir "Ingrese el tipo de Menbresia:"
    Leer tipoMembresia
	
    Escribir "Ingrese el Total de Compras:"
    Leer totalCompra
	
    //PRIMER DESCUENTO
    // SEGUN EL TIPO DE MENBRESÍA
    Segun tipoMembresia Hacer
	
    Caso "A":
        descuento <- totalCompra * 0.10
    	
    Caso "B":
        descuento <- totalCompra * 0.15
    	
    caso "C":
    	
        descuento <- totalCompra * 0.20
    	
    otrocaso:
        desceunto <- 0
	
FinSegun

//calcular el total a pagar 

totalConDescuento <- totalCompra - descuento

// Mostrar 
    escribir "Tipo de Menbresía:", tipoMembresia
    escribir "Total de Compra:", totalCompra  
    escribir "Descuento aplicado:", descuento
    escribir "Total con Descuento:", totalConDescuento
FinAlgoritmo */
