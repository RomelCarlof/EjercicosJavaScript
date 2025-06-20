# 1. Escribe una función que reciba una ruta de un fichero de texto y una cadena de caracteres a buscar y determine si la cadena aparece en el fichero.
import os

def existe_en_fichero(ruta_fichero, patron_a_buscar):
    with open(ruta_fichero, encoding= 'utf-8') as fichero:
        for linea in fichero:
            if patron_a_buscar in linea:
                return True

    return False

print(existe_en_fichero('res/Link_Paginas.txt', 'tres'))
print(existe_en_fichero('res/Link_Paginas.txt', 'Hola'))

