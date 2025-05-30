def merge_sort(arr):
    if len(arr) > 1:
        # Dividir el arreglo en dos mitades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamadas recursivas para cada mitad
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializamos índices
        i = j = k = 0

        # Combinar las mitades ordenadamente
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Añadir los elementos restantes de left_half (si hay)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Añadir los elementos restantes de right_half (si hay)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Lista original
numeros = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Ejecutamos el algoritmo
merge_sort(numeros)

# Mostramos el resultado
print("Lista ordenada:", numeros)
