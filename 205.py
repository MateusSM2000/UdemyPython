class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.deletar = None

p1 = Pessoa('Mateus',24)

print(p1.__dict__)
print(vars(p1))
print()

del p1.__dict__['deletar']
p1.__dict__['nome'] = 'Gabriele'
p1.__dict__['idade'] = 21
print(p1.__dict__)
print()

p2 = {'nome':'Marcia', 'idade':60}
p2 = Pessoa(**p2)
print(p2)
print(p2.__dict__)
print(p2.nome)
print(p2.idade)