def contenido_en_rango(numero,rango):
    return rango[0]<= numero <= rango[1]

rango = (1,5)

print(contenido_en_rango(5,rango))