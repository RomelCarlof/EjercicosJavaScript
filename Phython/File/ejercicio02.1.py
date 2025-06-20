# Escribe una función llamada escribir_objetos que reciba tres parámetros:
# - una lista de elementos (por ejemplo, strings o números),
# - una ruta de archivo de destino (como 'res/salida.txt'),
# - un número entero n.
# La función debe crear un archivo de texto en la ruta especificada, y escribir en él los primeros n elementos de la lista, uno por línea.
# La función debe validar que el valor de n sea correcto:
# - Si n es mayor que la longitud de la lista, debe lanzar una excepción o manejar el error con un mensaje.
# - Si n es negativo, también debe lanzar una excepción o mostrar un mensaje de advertencia.



def Escribir_ojetos(lista, ruta_fichero, n) : 
    with open(ruta_fichero, 'w') as fichero : 
        try:
            if(n < 0) : 
                raise IndexError
            for i in range(n):
                fichero.write(f"{lista[i]}\n")
            print(f"Fichero creado satisfactoriamente: se ingresaro {n} elementos en el fichero")
        except IndexError:
            print(f"Acceso fuera de rango. Valor n incorrecto: {n}. ")

Escribir_ojetos(['a','b','c','d','e','f','g'], 'res/Ejercio01.txt', 6)