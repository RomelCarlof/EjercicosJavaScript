#2. Escribe una función que reciba una lista, una ruta destino y un número n. La función debe crear un fichero en la ruta especificada. 
#   El contenido del fichero serán los primeros n elementos de la lista. La función debe controlar de manera apropiada los posibles valores
#   de n que estén fuera de rango.

def escribir_ojetos(lista, ruta_fichero, n):
    with open(ruta_fichero, 'w') as fichero:
        try:
            if(n < 0) :
                raise IndexError

            for i in range(n):
                fichero.write(f"{lista[i]}\n")
            
            print(f"Fichero creado sastisfactoriamente. Sw  escribieron {n} elementos en el fichero.")
        except IndexError:
            print(f"Acceso fuera de rango. Valor n incorrecto: {n}. ")

escribir_ojetos(['a', 'b', 'c', 'd', 'e', 'f'], 'res/Ejercicio2.txt', 9)
