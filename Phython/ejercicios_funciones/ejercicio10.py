
#9. Escribe una función que compruebe si un string dado es un palíndromo. Un palíndromo es una secuencia de caracteres que se lee igual de izquierda a derecha que de derecha a 
#izquierda. Por ejemplo, la función devolverá True si recibe el string "reconocer" y False si recibe el string "python".

def es_palindromo(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)- i - 1]:
            return False

    return True

print(es_palindromo("reconocer"))
print(es_palindromo("python"))