
HorasTrabajadas=int(input("Ingrese las horas trabajadas a la semana:"))

if HorasTrabajadas <= 40:
    SalarioBase = HorasTrabajadas * 20
else:
    SalarioBase = HorasTrabajadas * 20 + (HorasTrabajadas-40) * 25


#Mostrar resultados
print("trabajadas:", HorasTrabajadas)

print("Salario Base:", SalarioBase)

