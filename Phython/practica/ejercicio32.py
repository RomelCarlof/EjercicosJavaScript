# // 32. Se quiere saber cuál es la ciudad con mayor población
# //    Hay 3 provincias y 11 ciudades
# //    Algoritmo en JavaScript

# let provincias, ciudades;
# let i, j;
# let ciudadMayor, nombreCiudad;
# let poblacionMayor, poblacionActual;
# let provinciaMayor;

provincias = 3
ciudades = 11
poblacionMayor = 0
ciudadMayor = ""
provinciaMayor = 0

for i in range(1, provincias +1):
    print("Provincia ", i)

    for j in range(1, ciudades +1):
        nombreCiudad = input(f"Ingrese el nombre de la ciudad {j} de la provincia  {i}: ")
        poblacionActual = int(input(f"Ingrese la población de  {nombreCiudad} : "))

        if poblacionActual > poblacionMayor:
            poblacionMayor = poblacionActual
            ciudadMayor = nombreCiudad
            provinciaMayor = i;  #guardamos la provincia también
        

print("---------------------------------------------")
print(f"La ciudad con mayor población es: {ciudadMayor} con {poblacionMayor} habitantes (Provincia {provinciaMayor}).")
