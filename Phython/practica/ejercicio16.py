# Algoritmo DiaDeLaSemana
#Definir numero Como Entero

while True:
    numero = int(input("Ingrese un número del 1 al 7: "))
    if 1 <= numero <= 7:
        break
    else:
        print("Número inválido. Intente nuevamente.")

if numero == 1:
	print("Lunes")
		
elif numero == 2:
	print("Martes")
      
elif numero == 3:
	print("Miercoles")

elif numero == 4:
	print("Jueves")

elif numero == 5:
	print("Viernes")
	
elif numero == 2:
	print("Sabado")
	
elif numero == 2:
	print("Domingo")
	
else:
	print("Número inválido. Intente nuevamente.")
	