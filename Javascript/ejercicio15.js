//Algoritmo Convertidor_Pulgadas_Kilogramo
   let TotPulgadas;
   let LibrasCant;
   let CentimetroCant; 
   let TotKilo;
    
   CentimetroCant= parseFloat( prompt("Ingrese una cantidad en Centímetros:"));
   
    
 LibrasCant=parseFloat( prompt("Ingrese una cantidad en Libras:"));

    
    // Calcular conversiones
    TotPulgadas = CentimetroCant / 2.54
    TotKilo = LibrasCant * 0.453592
    
    // Mostrar resultados
    console.log( `TOTAL DE CÁLCULO EN PULGADAS:  ${TotPulgadas}`);
    alert( `TOTAL DE CÁLCULO EN PULGADAS:  ${TotPulgadas}`);
    console.log( `OTAL DE CÁLCULO EN KILOGRAMOS:   ${TotKilo}`);
    alert( `OTAL DE CÁLCULO EN KILOGRAMOS: ${TotKilo}`);    //template literal (plantilla literal),
