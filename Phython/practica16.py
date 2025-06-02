import csv
import requests

# URL del dataset
url = "https://raw.githubusercontent.com/grammakov/USA-cities-and-states/master/us_cities_states_counties.csv"

# Hacer la solicitud para obtener el contenido del CSV
response = requests.get(url)
data = response.text.splitlines()

# Inicializar el contador y la lista de ciudades
floridaCounter = 0
floridaCities = []

# Leer el CSV
for line in data:
    items = line.split("|")  # Dividir la línea por el delimitador '|'
    
    city = items[0]  # Obtener el nombre de la ciudad
    state = items[1]  # Obtener el estado
    
    # Verificar si el estado es Florida (FL) y si la ciudad no está ya en la lista
    if state == "FL" and city not in floridaCities:
        floridaCounter += 1  # Incrementar el contador
        floridaCities.append(city)  # Agregar la ciudad a la lista

# Mostrar el número de ciudades en Florida
print(f"Número de ciudades en Florida: {floridaCounter}")
