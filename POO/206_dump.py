import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Mateus', 24)
p2 = Pessoa('Gabriele', 21)
p3 = Pessoa('Marcia', 62)
p4 = Pessoa('Jaqueline', 33)
pessoas = [p1.__dict__,
      p2.__dict__,
      p3.__dict__,
      p4.__dict__
      ]

with open('206.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoas, arquivo, ensure_ascii=False, indent=2)