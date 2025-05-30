def merge_sort_visual(arr, depth=0):
    indent = "  " * depth  # Sangría para visualizar niveles

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        print(f"{indent}Dividir: {arr} → {left_half} | {right_half}")

        # Llamadas recursivas
        merge_sort_visual(left_half, depth + 1)
        merge_sort_visual(right_half, depth + 1)

        # Fusión
        i = j = k = 0

        print(f"{indent}Combinar: {left_half} + {right_half}")

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        print(f"{indent}Resultado: {arr}")
    else:
        print(f"{indent}Base: {arr}")

# Lista de entrada
numeros = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Ejecutar con visualización
print("=== Proceso de Merge Sort ===")
merge_sort_visual(numeros)
print("\n=== Lista final ordenada ===")
print(numeros)
