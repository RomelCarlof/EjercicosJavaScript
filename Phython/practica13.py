import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

colores = {
    1: "red",
    3: "yellow",
    4: "green",
    5: "blue"
}

# Estado inicial de las torres (discos de mayor a menor)
torres = {
    "Torre 1": [5, 4, 3, 1],  # Solo estos discos
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

# Variables para animación
disco_anim = torres["Torre 1"][-1]  # El disco más pequeño (el último)
ancho = disco_anim * 0.3
color = colores.get(disco_anim, "gray")

# Posición inicial del disco animado (sobre Torre 1)
x_inicio = posiciones["Torre 1"] - ancho / 2
y_inicio = 0.3 + (len(torres["Torre 1"]) - 1) * 0.4
disco_patch = patches.Rectangle((x_inicio, y_inicio), ancho, 0.3, color=color)
ax.add_patch(disco_patch)

# Dibujar los discos fijos que no se están moviendo
def dibujar_discos_fijos():
    for torre_nombre, discos in torres.items():
        if torre_nombre == "Torre 1":
            discos_fijos = discos[:-1]  # todos menos el último (que se mueve)
        else:
            discos_fijos = discos
        x_base = posiciones[torre_nombre]
        for idx, disco in enumerate(discos_fijos):
            ancho_d = disco * 0.3
            color_d = colores.get(disco, "gray")
            y = 0.3 + idx * 0.4
            ax.add_patch(patches.Rectangle((x_base - ancho_d / 2, y), ancho_d, 0.3, color=color_d))

dibujar_discos_fijos()

# Parámetros del movimiento
frames = 100
# El movimiento será: subir, mover horizontal, bajar
def update(frame):
    if frame < 30:
        # Subir
        y = y_inicio + frame * 0.05
        x = x_inicio
    elif frame < 70:
        # Mover horizontal
        y = y_inicio + 30 * 0.05
        dx = (posiciones["Torre 3"] - posiciones["Torre 1"]) * (frame - 30) / 40
        x = (posiciones["Torre 1"] - ancho / 2) + dx
    else:
        # Bajar
        y = y_inicio + 30 * 0.05 - 0.05 * (frame - 70)
        x = posiciones["Torre 3"] - ancho / 2

    disco_patch.set_xy((x, y))
    return [disco_patch]

anim = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.title("Animación: Movimiento de disco en Torres de Hanói", fontsize=14)
plt.show()
