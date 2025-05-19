#o def __del__() é executado logo antes da instancia ser deletada

class Cliente:
    enderecos = []
    def __init__(self,nome):
        self.nome = nome
        self.endereco = []

    def adicionar_endereco(self,estado,cidade,bairro,rua,numero):
        self.endereco.append(Endereco(estado,cidade,bairro,rua,numero))
        Cliente.enderecos.append([self.nome, Endereco(estado,cidade,bairro,rua,numero)])

    @staticmethod
    def listar_clientes():
        for cliente in Cliente.enderecos:
            print(f'Cliente: {cliente[0]}, endereço: {cliente[1].__dict__}')

    def __del__(self):
        print(f'APAGANDO {self.nome}')
        for cliente in Cliente.enderecos:
            if cliente[0] == self.nome:
                Cliente.enderecos.remove(cliente)

class Endereco:
    def __init__(self,estado,cidade,bairro,rua,numero):
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero



c1 = Cliente('Mateus')
c1.adicionar_endereco('SP','Limeira','Centro','Rua Boa Morte','260')
c2 = Cliente('Gabriele')
c2.adicionar_endereco('SP','Rio Claro', 'Jardim Kennedy', 'Rua PF4','216')
print(Cliente.enderecos)
Cliente.listar_clientes()
print()

del c2
try:
    print(c2.endereco)
except NameError:
    print('Instância não encontrada.')
print(Cliente.enderecos)
Cliente.listar_clientes()
print('##################### AKI TERMINA O CODIGO')