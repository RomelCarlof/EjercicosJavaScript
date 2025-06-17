#Escribe una función que reciba un número entero positivo como parámetro y devuelva una lista que contenga los 5 primeros múltiplos de dicho número. Por ejemplo, 
#si la función recibe el número 3, devolverá la lista [3, 6, 9, 12, 15]. Si la función recibe un parámetro incorrecto (por ejemplo, un múmero menor o igual a cero),
#mostrará un mensaje de error por pantalla y devolverá una lista vacía.

def contenido_en_rango(numero):
    if  numero <= 0 : 
        print("El número es incorrecto : debe ser mayor que cero") 
        return []


    multiplos = []

    for i in range(1,6): 
        multiplos.append(numero * i)
    return multiplos

print(contenido_en_rango(3))
print(contenido_en_rango(0))