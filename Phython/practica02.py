"""class Persona:
    def __init__(self, nombre):  # Constructor que recibe un nombre
        self.__nombre = nombre  # Almacena el nombre en el objeto
    
    def mostrar_nombre(self):  # Método correcto para mostrar el nombre
        print('Tu nombre es: ' + self.__nombre)

# Crear un objeto de la clase Persona
profesor = Persona('Romel')
profesor.mostrar_nombre()  # Llamar correctamente al método"""




"""class Persona:
    def __init__(self, apellido):
        self.__apellido = apellido

    def mostrar_apellido(self):
        print('Tu apellido es:' + self.__apellido)

profesor = Persona('Izaguirre Barbaran')
profesor.mostrar_apellido() """


class Ropa:
    def __init__(self, marca):
        self.__marca = marca

    def mostrar_marca(self):
        print('La marca de la Ropa es: ' + self.__marca)

salida  = Ropa('Bronco')
salida.mostrar_marca()