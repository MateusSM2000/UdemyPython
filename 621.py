#é oq eu utilizei pra fazer meu primeiro projeto

from abc import ABC, abstractmethod

class Conta(ABC):
    @abstractmethod
    def _sacar(self): pass

    def conectar_servidor(self):
        print('Conectando ao servidor...')

    def sacar(self):
        self.conectar_servidor()
        if self._sacar():
            print('Saque efetuado com sucesso!!')

class ContaCorrente(Conta):
    def _sacar(self):
        print('sacando da conta corrente...')
        return True


class ContaPoupanca(Conta):
    def _sacar(self):
        print('sacando da conta poupança...')
        return True


c1 = ContaPoupanca()
c2 = ContaCorrente()

c1.sacar()
print()
c2.sacar()