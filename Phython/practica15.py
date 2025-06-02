#Algoritmo CambioVoraz(C, monedas)
    #Ordenar monedas de mayor a menor
    #resultado ← lista vacía

    #Mientras C > 0 hacer
        #Para cada moneda en monedas hacer
            #Mientras moneda ≤ C hacer
                #Agregar moneda a resultado
                #C ← C - moneda

    #Retornar resultado


def cambio_voraz(cantidad, monedas):
    # Asegurarse de que las monedas estén ordenadas de mayor a menor
    monedas = sorted(monedas, reverse=True)
    resultado = []

    for moneda in monedas:
        while cantidad >= moneda:
            cantidad -= moneda
            resultado.append(moneda)

    return resultado

# PRUEBA DEL ALGORITMO
monedas_disponibles = [50, 25, 10, 5, 1]
cantidad_a_devolver = 63

resultado = cambio_voraz(cantidad_a_devolver, monedas_disponibles)

# MOSTRAR RESULTADO
print("Monedas entregadas:", resultado)
print("Número total de monedas:", len(resultado))
