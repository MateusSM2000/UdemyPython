#os parametros do return cls(parameteros) do @classmethod recebem os msms parametros q o do __init__. Ou seja esse classmethod serve para criar novas instancias
#com valores de parametros ja definidos

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_com_21_anos(cls, nome):
        return cls(nome, 21)

    @classmethod
    def criar_anonimo(cls,idade):
        return cls('Anônimo', idade)


p1 = Pessoa('Mateus', 24)
print(p1.__dict__)
print()

p2 = Pessoa.criar_com_21_anos('Gabriele')
print(p2.__dict__)
print(p2.nome)
print(p2.idade)
print()

p3 = Pessoa.criar_anonimo(33)
print(p3.__dict__)
print(p3.nome)
print(p3.idade)