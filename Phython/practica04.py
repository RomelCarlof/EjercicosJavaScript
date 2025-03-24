class Persona:
    def __init__(self, nombre, apellido, peso, altura):  # Constructor que recibe los parámetros
        self.__nombre = nombre  # Almacena el nombre en el objeto
        self.__apellido = apellido  # Almacena el apellido en el objeto
        self.__peso = peso  # Almacena el peso en el objeto
        self.__altura = altura  # Almacena la altura en el objeto

    def mostrar_nombre(self):  # Método correcto para mostrar el nombre (sin doble guion bajo)
        print(f'Tu nombre es: {self.__nombre} {self.__apellido}')  

    def IMC(self):  # Método para calcular y mostrar el IMC
        if self.__altura <= 0:
            print("Error: La altura debe ser mayor que 0")
            return
        imc = self.__peso / (self.__altura ** 2)  # Cálculo del IMC
        print(f'Tu IMC es: {imc:.2f}')  # Formato a 2 decimales

# Crear un objeto de la clase Persona
profesor = Persona('Romel', 'IZAGUIRRE BARBARAN', 85, 1.75)
profesor.mostrar_nombre()  # Llamar correctamente al método
profesor.IMC()  # Llamar al método IMC
