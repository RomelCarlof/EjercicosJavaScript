import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Colores de los discos
colores = {
    1: "red",
    2: "orange",
    3: "yellow",
    4: "green",
    5: "blue"
}

# Estado inicial de las torres (discos de mayor a menor)
torres = {
    "Torre 1": [5, 4, 3, 2, 1],  # Colocamos un disco adicional
    "Torre 2": [],
    "Torre 3": []
}

posiciones = {"Torre 1": 1.5, "Torre 2": 4.5, "Torre 3": 7.5}

fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 9)
ax.set_ylim(0, 6)
ax.axis('off')

# Dibujar torres (base y poste)
for x in posiciones.values():
    ax.add_patch(patches.Rectangle((x - 1, 0), 2, 0.3, color="black"))
    ax.add_patch(patches.Rectangle((x - 0.05, 0.3), 0.1, 4.7, color="black"))

# Función para realizar las animaciones
def mover_disco(torre_origen, torre_destino):
    disco = torres[torre_origen].pop()  # sacar el disco de la torre origen
    torres[torre_destino].append(disco)  # añadirlo a la torre destino
    return disco

# Implementar el algoritmo de Torres de Hanói
def hanoi(n, origen, destino, auxiliar, movimientos):
    if n == 1:
        movimientos.append((origen, destino))
    else:
        hanoi(n - 1, origen, auxiliar, destino, movimientos)
        movimientos.append((origen, destino))
        hanoi(n - 1, auxiliar, destino, origen, movimientos)

# Guardar todos los movimientos
movimientos = []
hanoi(len(torres["Torre 1"]), "Torre 1", "Torre 3", "Torre 2", movimientos)

# Definir función para dibujar discos
def dibujar_discos():
    for torre_nombre, discos in torres.items():
        x_base = posiciones[torre_nombre]
        for idx, disco in enumerate(discos):
            ancho_d = disco * 0.3
            color_d = colores.get(disco, "gray")
            y = 0.3 + idx * 0.4
            ax.add_patch(patches.Rectangle((x_base - ancho_d / 2, y), ancho_d, 0.3, color=color_d))

# Inicialización de la animación
disco_patch = None
frames = len(movimientos) * 20  # Cada movimiento generará múltiples frames

# Función de actualización
def update(frame):
    global disco_patch
    if frame % 20 == 0:  # Cada 20 frames se realiza un movimiento
        movimiento = movimientos[frame // 20]
        origen, destino = movimiento
        disco = mover_disco(origen, destino)

        ancho = disco * 0.3
        x_inicio = posiciones[origen] - ancho / 2
        y_inicio = 0.3 + (len(torres[origen]) - 1) * 0.4  # Calcular la nueva altura
        y_final = 0.3 + (len(torres[destino]) - 1) * 0.4  # Nueva posición vertical en destino

        # Crear la animación del disco
        if disco_patch is None:
            disco_patch = patches.Rectangle((x_inicio, y_inicio), ancho, 0.3, color=colores[disco])
            ax.add_patch(disco_patch)
        else:
            disco_patch.set_xy((x_inicio, y_inicio))
            disco_patch.set_width(ancho)

        # Simular movimiento vertical
        if frame % 20 < 10:  # Subir
            disco_patch.set_y(y_inicio + (frame % 20) * 0.05)
        else:  # Bajar
            disco_patch.set_y(y_inicio + 0.5 - (frame % 20 - 10) * 0.05)

        # Actualizar torres
        dibujar_discos()

    return [disco_patch]

anim = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.title("Animación: Movimiento de disco en Torres de Hanói", fontsize=14)
plt.show()
