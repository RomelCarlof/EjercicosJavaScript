#TECNICA VORAZ

def cambio_voraz(cantidad, monedas):
    resultado = []
    for moneda in monedas:
        while cantidad >= moneda:
            cantidad -= moneda
            resultado.append(moneda)
    return resultado

# Prueba
monedas = [50, 20, 10, 5, 1]
cambio = cambio_voraz(87, monedas)

print("Monedas usadas:", cambio)
print("Total de monedas:", len(cambio))
