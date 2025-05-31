def hanoi_restringido(n, origen, pivote, destino, movimientos):
    if n == 0:
        return

    # Paso 1: mover n discos de origen a destino, usando pivote como pivote (al revés)
    hanoi_restringido(n - 1, origen, pivote, destino, movimientos)

    # Paso 2: mover disco n de origen a pivote
    movimientos.append((origen, pivote))

    # Paso 3: mover n - 1 discos de destino a origen, usando pivote como pivote
    hanoi_restringido(n - 1, destino, pivote, origen, movimientos)

    # Paso 4: mover disco n de pivote a destino
    movimientos.append((pivote, destino))

    # Paso 5: mover n - 1 discos de origen a destino, usando pivote como pivote
    hanoi_restringido(n - 1, origen, pivote, destino, movimientos)

# Llamada al algoritmo
movimientos = []
hanoi_restringido(4, "Torre 1", "Torre 2", "Torre 3", movimientos)

# Mostrar los movimientos
for i, (origen, destino) in enumerate(movimientos, 1):
    print(f"{i}. Mover disco de {origen} a {destino}")

print(f"\nTotal de movimientos: {len(movimientos)}")
