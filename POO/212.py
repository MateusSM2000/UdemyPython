#o @property é um metodo q se transforma em um atributo. O nome do metodo se torna um atributo, e no return desse metodo está self.atributo
#isso serve para fazer com q codigos de terceiros q importam essa classe, n tenham problemas caso vc altere o nome do atributo
#isso pq terceiros vao estar pegando o nome do metodo como atributo, aí vc consegue mudar o nome do atributo pra qql coisa enquanto os terceiros vao estar utilizando o nome do
#metodo como atributo

class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta


c1 = Caneta('azul')
print(c1.cor)