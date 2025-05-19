def my_repr(cls):
    def my_repr_aux(self):
        return f'{self.__class__.__name__}({self.__dict__})'
    cls.__repr__ = my_repr_aux
    return cls


@my_repr
class Pais:
    def __init__(self, nome):
        self.nome = nome


@my_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome





brasil = Pais('Brasil')
eua = Pais('EUA')
portugal = Pais('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(Planeta.__repr__(brasil))   #ou seja a funcao my_repr adiciona manualmente a representaçao ao metodo __repr__ da classe
print(brasil)
print(eua)
print(portugal)
print(terra)
print(marte)