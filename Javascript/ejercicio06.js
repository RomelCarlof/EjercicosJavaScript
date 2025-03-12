let HorasTrabajadas;
let SalarioBase;
let SalarioTotal;

HorasTrabajadas=parseFloat(prompt("Ingrese las horas trabajadas a la semana:"));

if (HorasTrabajadas <= 40){
SalarioBase = HorasTrabajadas * 20;
}else{
SalarioBase = HorasTrabajadas * 20 + (HorasTrabajadas-40) * 25;
}

	//Mostrar resultados
console.log("trabajadas:" + HorasTrabajadas);
alert("trabajadas:" + HorasTrabajadas)
console.log("Salario Base:" + SalarioBase);
alert("Salario Base:" + SalarioBase)



/*//entonces las horas extras se le pagarán a $25 por hora.
Proceso Calculo_Salario
	Definir HorasTrabajadas Como Entero
	Definir SalarioBase, SalarioTotal Como Real
	
	Escribir "Ingrese las horas trabajadas a la semana:"
	Leer HorasTrabajadas
	
	Si HorasTrabajadas <= 40 Entonces
		SalarioBase = HorasTrabajadas * 20
	SiNo
		SalarioBase = HorasTrabajadas * 20 + (HorasTrabajadas-40) * 25
	FinSi
	
	//Mostrar resultados
	Escribir "Horas trabajadas:", HorasTrabajadas
    Escribir "Salario Base:", SalarioBase */
