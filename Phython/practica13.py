import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Colores definidos (sin el disco 2)
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

# Posiciones horizontales de cada torre
posiciones = {"Torre 1": 1.5, "Torre 2": 4.5, "Torre 3": 7.5}

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 9)
ax.set_ylim(0, 6)
ax.axis('off')

# Dibujar torres (base negra y poste)
for x in posiciones.values():
    # Base negra
    ax.add_patch(patches.Rectangle((x - 1, 0), 2, 0.3, color="black"))
    # Poste vertical
    ax.add_patch(patches.Rectangle((x - 0.05, 0.3), 0.1, 4.7, color="black"))

# Dibujar discos en la torre 1
x_base = posiciones["Torre 1"]
for idx, disco in enumerate(torres["Torre 1"]):
    ancho = disco * 0.3
    color = colores.get(disco, "gray")
    y = 0.3 + idx * 0.4
    ax.add_patch(patches.Rectangle((x_base - ancho / 2, y), ancho, 0.3, color=color))

# Título
plt.title("Torres de Hanói - Estado Inicial (Solo 4 discos)", fontsize=14)
plt.show()
