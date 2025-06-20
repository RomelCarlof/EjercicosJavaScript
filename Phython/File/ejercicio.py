# Crear un Fichero

import os  # 👈 IMPORTANTE

#def crear_lista(tamanyo):
 #   lista = []
  #  for i in range(tamanyo):
   #     lista.append(str(i) + '\n')
   # return lista

# Crear ruta relativa del archivo
ruta = os.path.join("res", "Link_Paginas.txt")

# Crear carpeta 'res' si no existe
os.makedirs(os.path.dirname(ruta), exist_ok=True)

# Escribir en el archivo
with open(ruta, 'wt', encoding='utf-8') as fichero:
    fichero.write("https://www.ejemplo.com\n")
    fichero.write("https://otra-url.com\n")

print("✅ Archivo creado correctamente en:", ruta)
