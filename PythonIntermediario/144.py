string = 'Mateus'
metodo = 'upper'
print(hasattr(string, metodo))
print(getattr(string, metodo))
print(bool(getattr(string, metodo)))