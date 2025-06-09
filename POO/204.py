#variaveis no escopo global podem ser acessadas dentro da classe e métodos. Variaveis definidas no corpo da classe n estão definidas no escopo global, mas podem serem
#modificadas fora do corpo da classe escrevendo nome_classe.variavel = ...

ano_atual = 1

class Pessoa:
    ano_atual = 2025

    def __init__(self,idade):
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

    def get_ano_nascimento_escopo_global(self):
        return ano_atual - self.idade


Mateus = Pessoa(24)
Gabriele = Pessoa(21)
print(Mateus.get_ano_nascimento())
print(Gabriele.get_ano_nascimento())
print()

print('ano_atual = 1 ; return ano_atual - self.idade')
print(Mateus.get_ano_nascimento_escopo_global())
print(Gabriele.get_ano_nascimento_escopo_global())
print()

Pessoa.ano_atual = 1
print('Pessoa.ano_atual = 1 ; return Pessoa.ano_atual - self.idade')
print(Mateus.get_ano_nascimento())
print(Gabriele.get_ano_nascimento())