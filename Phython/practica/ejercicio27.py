#Proceso Suma_cIEN_Numeros
#let suma;
#let i;

i = 1
suma = 0

while True:
    print(f"i vale:  {i}")
    suma += i
    i += 1 # Incrementa i
    if i <= 100:
        print(f"La suma de los 100 primeros numeros es: {suma}")
    break   

#FinProceso