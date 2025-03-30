class Persona:
    def __init__(self, nombre, apellido, direccion, telefono):  # Constructor que recibe un nombre
        self.__nombre = nombre; # Almacena el nombre en el objeto
        self.__apellido = apellido; 
        self.__direccion = direccion; 
        self.__telefono = telefono; 
      #  print(self.__apellido);
    
    def mostrar__nombre(self):  # Método correcto para mostrar el nombre
        print('Tu nombre es: ' + self.__nombre + ' ' + self.__apellido); 
        # print(f'Tu nombre es: {self.__nombre} {self.__apellido}')  # Usar f-strings para mejor legibilidad

    def mostrar__direccion(self):  # Método correcto para mostrar la dirección
        print('Tu direccion es: ' + self.__direccion); 
        # print(f'Tu nombre es: {self.__nombre} {self.__apellido}')  # Usar f-strings para mejor legibilidad

    def mostrar__telefono(self):  # Método correcto para mostrar la dirección
        print('Tu direccion es: ' + self.__telefono); 
        # print(f'Tu nombre es: {self.__nombre} {self.__apellido}')  # Usar f-strings para mejor legibilidad

# Crear un objeto de la clase Persona
profesor = Persona('Romel' , 'IZAGUIRRE BARBARAN', 'MICAELA BASTIDA N° 103', '994847647'); 
profesor.mostrar__nombre();  # Llamar correctamente al método
profesor.mostrar__direccion();  # Llamar correctamente al método
profesor.mostrar__telefono();  # Llamar correctamente al método
