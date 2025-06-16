#3. Escribe una función que reciba un string como entrada y devuelva el string al revés. Ejemplo: si el string de entrada es 'hola', el resultado será 'aloh'.

def invertir(s):

    Invertida = ""
    for caracter in s : 
        Invertida = caracter + Invertida
    return Invertida

print(invertir("Hola"))