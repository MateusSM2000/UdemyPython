#quando vc faz um objeto receber um objeto de uma classe, acontece a msm coisa q acontece quando faz um objeto receber uma lista ou dicionário. há um espelhamento entre eles
# e qualquer mudança feita é universal. se mudar qql coisa em qql um deles, vai mudar pra tds. no caso de classes o unico jeito de contornar isso é usando a função deepcopy()
# do módulo copy

from copy import deepcopy


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f'{self.nome}'

    def copy(self):
        return deepcopy(self)

p1 = Pessoa('Mateus')
p2 = p1
print(p1, p2)
p2.nome = 'Marcinha'
print(p1, p2)
print()

p3 = p1.copy()
p3.nome = 'Mateus'
print(p1, p3)