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
    # Ordenamos las monedas de mayor a menor
    monedas.sort(reverse=True)
    resultado = []

    for moneda in monedas:
        # Mientras podamos usar esta moneda
        while cantidad >= moneda:
            cantidad -= moneda
            resultado.append(moneda)
            print(f"Usamos moneda: {moneda}, queda por devolver: {cantidad}")

    return resultado

# Ejemplo de uso
monedas_disponibles = [50, 25, 10, 5, 1]
cantidad_a_devolver = 63

solucion = cambio_voraz(cantidad_a_devolver, monedas_disponibles)

print("\nMonedas entregadas:", solucion)
print("Número total de monedas:", len(solucion))

