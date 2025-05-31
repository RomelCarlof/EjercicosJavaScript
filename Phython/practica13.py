import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Colores para los discos
colores = {
    1: "red",
    2: "orange",
    3: "yellow",
    4: "green",
    5: "blue"
}

# Configuración inicial de las torres (de mayor a menor)
torres = {
    "Torre 1": [5, 4, 3, 2, 1],
    "Torre 2": [],
    "Torre 3": []
}

# Posiciones de las torres en el gráfico
posiciones = {"Torre 1": 1.5, "Torre 2": 4.5, "Torre 3": 7.5}

# Crear la imagen de referencia basada en el estilo proporcionado
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 9)
ax.set_ylim(0, 6)
ax.axis('off')

# Dibujar bases negras de cada torre
for x in posiciones.values():
    ax.add_patch(patches.Rectangle((x - 1, 0), 2, 0.3, color="black"))  # Base
    ax.add_patch(patches.Rectangle((x - 0.05, 0.3), 0.1, 4.7, color="black"))  # Poste

# Dibujar los discos en la Torre 1
base_x = posiciones["Torre 1"]
for j, disco in enumerate(torres["Torre 1"]):
    ancho = disco * 0.3
    color = colores.get(disco, "gray")
    ax.add_patch(patches.Rectangle((base_x - ancho/2, 0.3 + j * 0.4), ancho, 0.3, color=color))

plt.title("Estado inicial: Todos los discos en Torre 1")
plt.show()
