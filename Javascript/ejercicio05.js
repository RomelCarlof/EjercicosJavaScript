// Defición de cada variable
let CantidadZapatos;
let TotalConDescuento;
let TotalCompras;
let Descuento;
// Constante que representa el precio de cada zapato
let PrecioZapato = 80;


// Verificar que la entrada sea válida
if (isNaN(CantidadZapatos) || CantidadZapatos <= 0) {
    alert("Por favor, ingrese una cantidad válida de zapatos.");
} else {
    // Calcular el total de la compra sin descuento
    TotalCompras = CantidadZapatos * PrecioZapato;
}
//aplicando Descuento

if (CantidadZapatos > 30) {
    Descuento = 0.4; //descuento al 40%

} else if (CantidadZapatos > 20) {
    Descuento = 0.2; // descuento al 20% 

} else if (CantidadZapatos > 10) {
    Descuento = 0.1; // descuento al 10% 
} else {
    Descuento = 0;  // no se aplica Descuento
}

// Calcular el total con descuento
TotalConDescuento = TotalCompras - (TotalCompras * Descuento);


// Mostrar resultados en consola y alertas
console.log("Cantidad de zapatos: " + CantidadZapatos);
alert("Cantidad de zapatos: " + CantidadZapatos);

console.log("Precio por zapato: " + PrecioZapato);
alert("Precio por zapato: " + PrecioZapato);

console.log("Total de la compra sin descuento: " + TotalCompras);
alert("Total de la compra sin descuento: " + TotalCompras);

console.log("Descuento aplicado: " + (Descuento * 100) + "%");
alert("Descuento aplicado: " + (Descuento * 100) + "%");

console.log("Total con descuento: " + TotalConDescuento);
alert("Total con descuento: " + TotalConDescuento);


/*
Proceso Calcula_Descuentos
    // Constante que representa el precio de cada zapato
    PrecioZapato<- 80
	
    // Defición de cada variable
    Definir CantidadZapatos Como Entero
    Definir Totaldescuento,TotalCompras, Descuento Como real
	
    // Entrada de Datos
    Escribir "Ingrese la cantidad de Zapatos va comprar de acuerdo a eso se le aplicara el descuento respectivo:"
    Leer CantidadZapatos
	
    // Calcular el total de compra sin Descuento
	
    TotalCompras= CantidadZapatos*PrecioZapato
	
    //aplicando Descuento
	
    Si CantidadZapatos > 30 Entonces
        Descuento <- 0.4 //descuento al 40%
    	
    SiNo
        Si CantidadZapatos > 20 Entonces
            Descuento <- 0.2 // descuento al 20% 
        SiNo
            Si CantidadZapatos > 10 Entonces
                Descuento <- 0.1 // descuento al 10% 
            SiNo
                Descuento <- 0  // no se aplica Descuento
            FinSi
        FinSi
    FinSi
    // Calcular el total con descuento
    totalConDescuento <- totalCompras - (totalCompras * descuento)
     //Mostrar resultados
    Escribir "Cantidad de zapatos:", CantidadZapatos
    Escribir "Precio por zapato:", PrecioZapato
    Escribir "Total de la compra sin descuento:", totalCompras
    Escribir "Descuento aplicado:", descuento * 100, "%"
    Escribir "Total con descuento:", totalConDescuento*/
	