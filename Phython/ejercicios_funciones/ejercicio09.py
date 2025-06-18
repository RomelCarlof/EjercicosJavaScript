#8. Escribe una función lambda que, al igual que la función desarrollada en el ejercicio anterior, reciba una lista como parámetro y compruebe si la lista tiene duplicados. 
#La función devolverá True si la lista tiene duplicados y False si no los tiene.
#Operador	Significado
#==	Igual a
#!=	Distinto de
#<	Menor que
#>	Mayor que
#<=	Menor o igual
#>=	Mayor o igual


contiene_duplicados = lambda lista : len(lista) != len(set(lista)) #!= significa que es distinto de 

print(contiene_duplicados([1,2,3,4,5]))
print(contiene_duplicados([1,2,3,4,5,5,5]))    
