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
                print(f"Par encontrado: ({i}, {j})")
                conteo_cruzado += 1

    # Llamadas recursivas
    conteo_izquierda = contar_pares(izquierda, k)
    conteo_derecha = contar_pares(derecha, k)

    return conteo_cruzado + conteo_izquierda + conteo_derecha


arr = [1, 5, 3, 7, 2, 4]
k = 6
total = contar_pares(arr, k)
print(f"Total de pares que suman {k}: {total}")