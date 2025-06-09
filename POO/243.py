class MyRepr:
    def __repr__(self):
        return f'{self.__class__.__name__}({self.__dict__})'


class Pais(MyRepr):
    def __init__(self, nome):
        self.nome = nome


class Planeta(MyRepr):
    def __init__(self, nome):
        self.nome = nome



brasil = Pais('Brasil')
eua = Pais('EUA')
portugal = Pais('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(eua)
print(portugal)
print(terra)
print(marte)