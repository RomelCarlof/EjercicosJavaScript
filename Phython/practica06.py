class Persona:
    def __init__(self, nombre, apellido, peso, altura):  # Constructor que recibe los parámetros
        self.__nombre = nombre;  # Almacena el nombre en el objeto
        self.__apellido = apellido; # Almacena el apellido en el objeto
        self.__peso = peso;  # Almacena el peso en el objeto
        self.__altura = altura;  # Almacena la altura en el objeto

    def mostrar__nombre(self):  # Método correcto para mostrar el nombre
        print('Tu nombre es: ' + self.__nombre + ' ' + self.__apellido);
        # print(f'Tu nombre y apellido es: {self.__nombre} {self.__apellido}')  # Usar f-strings para mejor legibilidad

    def IMC(self):  # Método para calcular y mostrar el IMC
        try:
            print('Tu IMC ES  PESO KG/ESTATURA M2:');
            print(self.__peso / (self.__altura * self.__altura));
        except ZeroDivisionError as e:
            print('Seguramente el peso es 0');
        finally:
            print('Fin del cálculo IMC');

while True:
    nombre = input('Dime tu nombre');
    apellido = input('Dime tu apellido');
    peso = float(input('Dime tu peso en kg'));
    altura = float(input('Dime tu altura en m'));

    p = Persona(nombre, apellido, peso, altura)
    p.IMC()





# Crear un objeto de la clase Persona
# profesor = Persona('Romel' , 'IZAGUIRRE BARBARAN', 85, 1.75)
# profesor.mostrar__nombre();  # Llamar correctamente al método
# profesor.IMC()  # Llamar al método IMC


