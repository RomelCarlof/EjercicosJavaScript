
descuento = 0  # Inicializar en 0 para evitar errores


tipoMembresia = input("Ingrese el tipo de Menbresía (A,B,C):").toUpperCase()

totalCompra = int(input("Ingrese el total de la compra:"))


# PRIMER DESCUENTO
# SEGUN EL TIPO DE MENBRESÍA

try:
    totalCompra = float(input("Por favor, ingrese una cantidad válida de zapatos."))

except ValueError:
    print("Por favor, ingrese una cantidad válida de zapatos.")
    exit()

# Validar si el número ingresado es positivo 
if totalCompra <= 0:
    print("Por favor, ingrese una cantidad válida de zapatos.")
    exit()

# Solicitar tipo de membresía

tipoMembresia = input("Ingrese el tipo de membresía (A, B, C): ").upper() # upper sirve para poner todo en mayuscula


# Simulación de un switch con un diccionario

descuentos ={
    "A": totalCompra * 0.10,
    "B": totalCompra * 0.15,
    "C": totalCompra * 0.20
}
# Si el tipo de membresía no está en el diccionario, asignamos descuento 0
descuento = descuento.get(tipoMembresia, 0)
 
#calcular el total a pagar 

totalConDescuento = totalCompra - descuento

#Mostrar 
print("Tipo de Menbresía:", tipoMembresia)
print("Total de Compra:", round( totalCompra, 2)) # cualquiera de los dos es valido
print(f"Descuento aplicado: {descuento:.2f}") # cualquiera de lmos dos es valido 
print(f"Total con descuentoo: {totalConDescuento:.2f}") # cualquiera de lmos dos es valido 
