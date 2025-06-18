#Escribe una función que compruebe si un número se encuentra dentro de un rango específico.

def contenido_en_rango(numero,rango):
    return numero in range(rango[0], rango[1])

rango = (1,7)

print(contenido_en_rango(2,rango))
print(contenido_en_rango(6,rango))