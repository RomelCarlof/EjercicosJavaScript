#31. Hacer un algoritmo en Pseint parar calcular la media de los números pares e impares, sólo se ingresará diez números.
#Proceso Media123
   
Suma = 0;  # Se usa una variable para acumular la suma
Contador = 0;  # Se usa para contar los números sumados

for i in range(0, 10, 2):
    print("Escribir:",i)
    Suma = Suma + i
    Contador =Contador + 1  # Contamos los números sumados
   
Media = Suma / Contador # Se calcula la media al final

print("La media de los números pares de 10 números ingresados es: ", Media)
   
