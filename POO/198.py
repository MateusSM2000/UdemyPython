#as funções nas classes sao chamadas de métodos. E as regras são as msms q funções foras de classes. A unica diferença é a presença do self (instancia, nesse caso p1 e p2)


class Pessoa:
    ...

p1 = Pessoa
p1.nome = 'Mateus'
p1.sobrenome = 'Schmidt Mesquita'

p2 = Pessoa()
p2.nome = 'Gabriele'
p2.sobrenome = 'Borges'

print(p1.nome, p1.sobrenome)
print(p2.nome, p2.sobrenome)
