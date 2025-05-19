#é possivel utilizar os atributos de uma instância de uma classe em outra classe jogando essa instancia em outra classe
#ai nesse caso conseguimos usar produto.nome e produto.preco pq é a instancia em si q tá na lista do carrinho._produtos, e n os p1.__dict__ e p2.__dict__

class Carrinho:
    def __init__(self):
        self._produtos = []

    @property
    def produtos(self):
        return self._produtos

    @produtos.setter
    def produtos(self, valor):
        self._produtos = valor

    def listar_carrinho(self):
        print(f'{'Produto':<25}{'Preço'}')
        print('-'*35)
        for produto in self._produtos:
            print(f'{produto.nome:<25}R${produto.preco:>8.2f}')
        print('-' * 35)
        print(f'Total: R${self.total_preco():.2f}')

    def adicionar_ao_carrinho(self,*produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def total_preco(self):
        s = 0
        for produto in self._produtos:
            s += produto.preco
        return s


class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco



carrinho = Carrinho()
p1 = Produto('S23',3300)
p2 = Produto('Tablet S9 Ultra',6300)
carrinho.adicionar_ao_carrinho(p1,p2)
print(carrinho.produtos)
#essa instancia dentro da lista nao é iteravel, portanto n dá pra fazer dict(instancia)
carrinho.listar_carrinho()