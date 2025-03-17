x = 50
print(id(x))  # ID inicial

x += 10  # Se crea un nuevo objeto
print(id(x))  # Nuevo ID, ya que los enteros son inmutables
