from decimal import Decimal, getcontext

# Configurar la precisión a 1000 dígitos
getcontext().prec = 1000

# Operación con Decimal
resultado = Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")

# Mostrar el resultado
print(resultado)  # Debería imprimir 0.0

V= True
f = False  

# str.capitalize()  Regresa la lista de caracteres inicial pero poniendo la primera letra en mayúscula.
# str.isalpha()  Regreso Verdadero si la lista de caracteres es no vacía y todos los caracteres son letras. En la figura 15 podemos ver que no regresa Falso, pues tenemos '!' que no es considerado una letra.
# str.isdigit() Regreso Verdadero si la lista de caracteres es no vacía y todos los caracteres son números. En la figura 15 podemos ver que una cadena no está compuesta por puros números.