#Escribe una función que reciba una lista como parámetro y compruebe si 
#la lista tiene duplicados. La función devolverá True si la lista tiene duplicados y False si no los tiene.

def contiene_duplicados(lista):
    objetos_ya_vistos = set ()


    for objeto in lista:
        if objeto in objetos_ya_vistos:
            return True
        objetos_ya_vistos.add(objeto)
      
    return False

print(contiene_duplicados([1,2,3,4,5]))
print(contiene_duplicados([1,2,3,4,5,5,5]))    
