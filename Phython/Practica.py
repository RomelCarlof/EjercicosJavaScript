from decimal import Decimal, getcontext

# Configurar la precisión a 1000 dígitos
getcontext().prec = 1000

# Operación con Decimal
resultado = Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")

# Mostrar el resultado
print(resultado)  # Debería imprimir 0.0
