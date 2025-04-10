Paga= float(input("Ingrese el Pago por mes:"))

# SUELDO POR MES
	# SEGUN EL TIPO DE PAGO
if Paga <= 2000:
	AumentoTotal= (Paga+(Paga*0.10))
	#// Mostrar 
	print("Tipo de Paga con Aumento" , " " , AumentoTotal)


else:
	AumentoTotal=(Paga+(Paga*0.05))
	#Mostrar 
	print(f"Tipo de Paga con Aumento: {AumentoTotal:2f}");  #Backticks (``) son útiles cuando necesitas incluir variables dentro de un string sin usar concatenación (+`).
       
	