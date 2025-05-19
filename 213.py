#convenção: atributos ou métodos que começar com um underlines não devem ser usados fora da classe.
#convenção: atributos ou métodos que começar com dois underlines não devem ser usados fora da classe e nem podem ser usados em subclasses.
#o setter deixa alterar qql valor de self.atributo da classe, usando o atributo fake criado pelo property

class Caneta:
    def __init__(self,cor):
        self._cor_tinta = cor
        self.esferografica = None

    @property
    def cor(self):
        return self._cor_tinta

    @cor.setter
    def cor(self, valor):
        self._cor_tinta = valor
        self.esferografica = True


c1 = Caneta('azul')
print(c1.__dict__)
c1.cor = 'vermelha'
print(c1.__dict__)