class Persona:
    def __init__(self, nombre):  # Constructor que recibe un nombre
        self.__nombre = nombre  # Almacena el nombre en el objeto
    
    def mostrar_nombre(self):  # Método correcto para mostrar el nombre
        print('Tu nombre es: ' + self.__nombre)

# Crear un objeto de la clase Persona
profesor = Persona('Romel')
profesor.mostrar_nombre()  # Llamar correctamente al método
