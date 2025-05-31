#o init faz com q, no momento em q uma instancia da classe é criada, a função __init__ é automaticamente executada
#os códigos dentro da classe q n são métodos ou funções, são executados apenas uma vez logo quando roda o programa
#as variaveis declaradas dentro da classe mas fora de metodos ou funcoes (atributos da classe) e os atributos do objeto sao declaradas no escopo global
#atributos da classe sao acessados com 'classe.variavel' e tbm se tornam atributos das instâncias,
# mas elas NAO sao conectadas entre si apesar do atributo do objeto receber o msm valor quando criado. se um mudar o outro n muda

class Pessoa:
    print('a')
    especie = 'ser humano'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        print(self.especie)

p1 = Pessoa('Mateus','Schmidt Mesquita')
p2 = Pessoa('Gabriele','Borges')
print()

print(p1.nome,p1.sobrenome)
print(p2.nome,p2.sobrenome)
print(p1.especie)
print(p2.especie)
print()

print(Pessoa.especie)
p1.especie = 'humano'
print(p1.especie)
print(Pessoa.especie)
Pessoa.especie = 'humano'
print(Pessoa.especie)
p3 = Pessoa('Marcos','Batista')