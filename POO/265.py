#dataclass é uma funcao decoradora para a criação de classes q já executa algumas coisas sem a necessidade de escrever no código, mas com algumas limitacoes
#pode criar metodos normalmente, como se estivesse criando sem usar o dataclass

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

    def __call__(self, *args, **kwargs):
        print(f'Executando a instância {self}')

    def andar(self):
        print(f'{self.nome} está andando.')

p1 = Pessoa('Mateus', 24)
p2 = Pessoa('Mateus', 24)
print(p1)
print(p1.nome)
print(p1.__dict__)
print(p1 == p2)
p1.andar()
p1()