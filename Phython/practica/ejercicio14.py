def numero_primo_case():
    while True:
        entrada = input("Ingrese un número entero positivo (1..10): ").strip()

        if not entrada.isdigit():
            print("Entrada inválida. Debe ser un número entero positivo.")
            continue  # vuelve al inicio del while

        n = int(entrada)

        if n < 1 or n > 10:
            print("El número está fuera del rango esperado.")
            continue  # vuelve a pedir otro número

        # Si el número está dentro del rango, evaluamos si es primo o no
        if n == 1:
            print("No es primo")  # 1 no se considera primo
        elif n in [2, 3, 5, 7]:
            print("Es primo")
        else:
            print("No es primo")
        
        break  # salir del bucle

# Ejecutar función
numero_primo_case()
