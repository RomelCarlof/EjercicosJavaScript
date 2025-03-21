class Persona:
    def __init__(self, nombre, apellido):  # Constructor que recibe un nombre
        self.__nombre = nombre; # Almacena el nombre en el objeto
        self.__apellido = apellido;
      #  print(self.__apellido);
    
    def mostrar__nombre(self):  # Método correcto para mostrar el nombre
        print('Tu nombre es: ' + self.__nombre + ' ' + self.__apellido);
        # print(f'Tu nombre es: {self.__nombre} {self.__apellido}')  # Usar f-strings para mejor legibilidad

# Crear un objeto de la clase Persona
profesor = Persona('Romel' , 'IZAGUIRRE BARBARAN');
profesor.mostrar__nombre();  # Llamar correctamente al método
