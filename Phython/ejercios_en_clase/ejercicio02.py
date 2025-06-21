# Dataset -> https://raw.githubusercontent.com/grammakov/USA-cities-and-states/master/us_cities_states_counties.csv
# Header -> City|State short|State full|County|City alias
# Obtener el número de ciudades que tiene el estado de Florida, usando dicho Dataset
# Sin usar Pandas

url = "https://raw.githubusercontent.com/grammakov/USA-cities-and-states/master/us_cities_states_counties.csv"

# Devuelve un fichero desde una url como cadena de caracteres
def read_url(url):
    return urllib.request.urlopen(url).read().decode('utf-8')

# Descargar un fichero desde una url a una ruta local
def download_file(url, dest):
    urllib.request.urlretrieve(url, dest)
    return


content = read_url()
print(content)