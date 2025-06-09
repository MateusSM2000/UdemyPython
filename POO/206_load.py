import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

with open('206.json', 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    print(pessoas)
    print()

p1 = Pessoa(**pessoas[0])
p2 = Pessoa(**pessoas[1])
p3 = Pessoa(**pessoas[2])
p4 = Pessoa(**pessoas[3])

print(p1)
print(p1.__dict__)
print(p1.nome)
print(p1.idade)
print()

print(p2)
print(p2.nome)
print()

print(p3)
print(p3.nome)
print()

print(p4)
print(p4.nome)
print()