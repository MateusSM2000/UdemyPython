#o init faz com q, no momento em q uma instancia da classe é criada, a função __init__ é automaticamente executada
#os códigos dentro da classe q n são métodos ou funções, são executados apenas uma vez logo quando roda o programa
#os atributos da classe tbm se tornam atributos das instâncias

class Pessoa:
    print('a')
    especie = 'ser humano'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Mateus','Schmidt Mesquita')
p2 = Pessoa('Gabriele','Borges')

print(p1.nome,p1.sobrenome)
print(p2.nome,p2.sobrenome)
print(p1.especie)
print(p2.especie)