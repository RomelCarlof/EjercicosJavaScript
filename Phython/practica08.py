import numpy as np
import matplotlib.pyplot as plt

# Rango de valores de x
x = np.linspace(0, 10, 100)

# Funciones
f_x = 2 * x**3 + x
g_x = x**3

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, f_x, label='f(x) = 2x^3 + x', color='blue')
plt.plot(x, g_x, label='g(x) = x^3', color='orange', linestyle='--')

# Configuración de la gráfica
plt.title('Comparación de O(2x^3 + x) y O(x^3)')
plt.xlabel('x')
plt.ylabel('Valor de la función')
plt.legend()
plt.grid()
plt.ylim(0, 300)  # Ajustar el límite del eje Y para mejor visualización
plt.xlim(0, 10)   # Ajustar el límite del eje X
plt.show()
