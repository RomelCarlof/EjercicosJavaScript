def contar_pares(arr, k):
    n = len(arr)
    if n <= 1:
        return 0

    mitad = n // 2
    izquierda = arr[:mitad]
    derecha = arr[mitad:]

    # Conteo cruzado: todos contra todos entre izquierda y derecha
    conteo_cruzado = 0
    for i in izquierda:
        for j in derecha:
            if i + j == k:
                conteo_cruzado += 1

    # Llamadas recursivas
    conteo_izquierda = contar_pares(izquierda, k)
    conteo_derecha = contar_pares(derecha, k)

    return conteo_cruzado + conteo_izquierda + conteo_derecha