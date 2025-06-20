# 3. Escribe una función que reciba una ruta de un fichero de texto devuelva un diccionario con la frecuencia de aparición de cada palabra. 
# Ejemplo: un fichero que contenga la frase 'es mejor que venga que que no venga' devolverá el siguiente diccionario: {'es' : 1, 'mejor' : 1, 'que' : 3, 'venga' : 2, 'no' : 1}.
# Para dividir un string en palabras puedes hacer uso del método split.

def anyadir_palabra(frecuencias, palabra):
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

def obtener_frecuencias(ruta_fichero):
    frecuencias = {}
    with open(ruta_fichero, encoding='utf-8') as fichero:
        for linea in fichero:
            for palabra in linea.split():
                anyadir_palabra(frecuencias, palabra)
    return frecuencias

obtener_frecuencias('res/Ejercicio3.txt')
