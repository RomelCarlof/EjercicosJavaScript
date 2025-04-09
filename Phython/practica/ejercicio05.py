
# Constante que representa el precio de cada zapato
PrecioZapato = 80


# Verificar que la entrada sea válida
try: 
    CantidadZapatos = int(input("Por favor, ingrese una cantidad válida de zapatos."))

except ValueError:
     print("Por favor, ingrese una cantidad válida de zapatos.")
     exit()

# Validar si el número ingresado es positivo

if CantidadZapatos <= 0:
     print("Por favor, ingrese una cantidad válida de zapatos.")

else :
    # Calcular el total de la compra sin descuento
    TotalCompras = CantidadZapatos * PrecioZapato;

#aplicando Descuento

if CantidadZapatos > 30:
    Descuento = 0.4; #descuento al 40%

elif CantidadZapatos > 20:
    Descuento = 0.2; # descuento al 20% 

elif CantidadZapatos > 10:
    Descuento = 0.1; # descuento al 10% 
else:
    Descuento = 0;  # no se aplica Descuento


# Calcular el total con descuento
TotalConDescuento = TotalCompras - (TotalCompras * Descuento)


# Mostrar resultados en consola y alertas

print("Cantidad de zapatos: " , CantidadZapatos)


print("Precio por zapato: " , PrecioZapato)

print("Total de la compra sin descuento: " , TotalCompras)

print("Descuento aplicado: " , int (Descuento * 100), "%")

print("Total con descuento: " , TotalConDescuento)
