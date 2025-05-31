import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Colores definidos (sin el disco 2)
colores = {
    1: "red",
    3: "yellow",
    4: "green",
    5: "blue"
}

# Estado inicial de las torres
torres = {
    "Torre 1": [5, 4, 3, 1],  # Solo estos discos
    "Torre 2": [],
    "Torre 3": []
}

# Posiciones horizontales de cada torre
posiciones = {"Torre 1": 1.5, "Torre 2": 4.5, "Torre 3": 7.5}

# Variables para guardar el estado de la selección
selected_tower = None
selected_disk = None

# Función para dibujar el estado actual de las torres
def dibujar():
    ax.clear()
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Dibujar torres (base negra y poste)
    for x in posiciones.values():
        ax.add_patch(patches.Rectangle((x - 1, 0), 2, 0.3, color="black"))
        ax.add_patch(patches.Rectangle((x - 0.05, 0.3), 0.1, 4.7, color="black"))

    # Dibujar discos en las torres
    for torre, discos in torres.items():
        x_base = posiciones[torre]
        for idx, disco in enumerate(discos):
            ancho = disco * 0.3
            color = colores.get(disco, "gray")
            y = 0.3 + idx * 0.4
            ax.add_patch(patches.Rectangle((x_base - ancho / 2, y), ancho, 0.3, color=color))

    plt.title("Torres de Hanói - Estado Actual", fontsize=14)
    plt.draw()

# Función para manejar clics en el gráfico
def on_click(event):
    global selected_tower, selected_disk

    # Determina la torre seleccionada
    if event.xdata is not None and event.ydata is not None:
        for torre, x in posiciones.items():
            if x - 1 < event.xdata < x + 1:
                if selected_tower is None:  # Selecciona la torre
                    selected_tower = torre
                    if torres[torre]:
                        selected_disk = torres[torre][-1]  # Selecciona el disco superior
                else:  # Intenta mover el disco a otra torre
                    if (not torres[torre] or (selected_disk < torres[torre][-1])):
                        # Mueve el disco
                        torres[torre].append(torres[selected_tower].pop())
                    selected_tower = None
                    selected_disk = None  # Reinicia la selección
                dibujar()  # Redibuja el estado

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(10, 5))
dibujar()  # Dibuja el estado inicial

# Conectar el evento de clic
cid = fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()
