def numero_primo_case():
    n = int(input("Ingrese un número entero positivo (1..9 o 1..10): "))

    if n == 1:
        print("No es primo")  # 1 no se considera primo
    elif n == 2:
        print("Es primo")
    elif n == 3:
        print("Es primo")
    elif n == 4:
        print("No es primo")
    elif n == 5:
        print("Es primo")
    elif n == 6:
        print("No es primo")
    elif n == 7:
        print("Es primo")
    elif n == 8:
        print("No es primo")
    elif n == 9:
        print("No es primo")
    elif n == 10:
        print("No es primo")
    else:
        print("El número está fuera del rango esperado.")

# Llamar a la función
numero_primo_case()
