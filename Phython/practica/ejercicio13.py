while True:
    letra = input("Ingrese una letra: ").strip()  # Eliminar espacios en blanco

    # Validar que solo se haya ingresado una letra y que no sea un número
    if len(letra) == 1 and letra.isalpha():
        break
    else:
        print("Por favor, ingrese solo una letra.")


# Convertir a minúscula para simplificar la comparación
letra = letra.lower()

if letra in ["a", "e", "i", "o", "u"]:
    print("La letra es una vocal")
else:
    print("La letra no es una vocal")
