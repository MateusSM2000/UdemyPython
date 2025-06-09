from abc import ABC, abstractmethod
from re import fullmatch
from pathlib import Path
import json

class Banco:
    """
    :self.clientes: lista com todos os dados de cada cliente cadastrado
    """
    def __init__(self, cliente=None):
        self.cliente : None|Cliente = cliente
        with open(Path(__file__).parent / 'santander.json', 'r', encoding='utf_8') as santander_cpf_db:
            self._clientes = json.load(santander_cpf_db)

    @staticmethod
    def dump_santander_json(self_clientes) -> None:
        with open(Path(__file__).parent / 'santander.json', 'w', encoding='utf_8') as santander_cpf_db:
            json.dump(self_clientes, santander_cpf_db, ensure_ascii=False, indent=2)

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self, clientes):
        self._clientes = clientes



#--------------------------------------------------------------------------------------------------------



class Cliente:
    def __init__(self, cliente_:dict[str, dict], conta_poupanca=None, conta_corrente=None):
        """
        :param cliente_: dicionário primário da lista em santander.json
        """
        for cpf_ in cliente_.keys():
            if fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf_):
                cpf = cpf_
                break
        cliente__encontrado = False
        for cliente_ in Banco().clientes:
            for cpf_ in cliente_.keys():
                if cpf_ == cpf:
                    cliente = cliente_
                    cliente__encontrado = True
                    break
            if cliente__encontrado:
                break
        self.cpf = cpf
        self.nome = cliente[cpf]['nome']
        self.data_nascimento = cliente[cpf]['data_nascimento']
        self.numero_telefone = cliente[cpf]['numero_telefone']
        self.email = cliente[cpf]['email']
        self.agencia = cliente[cpf]['agencia']
        self.numero_conta = cliente[cpf]['numero_conta']
        self.saldo_corrente = cliente[cpf]['saldo_corrente']
        self.saldo_poupanca = cliente[cpf]['saldo_poupanca']
        self.data_criacao_conta = cliente[cpf]['data_criacao_conta']
        self.conta_poupanca : ContaPoupanca|None = conta_poupanca
        self.conta_corrente : ContaCorrente|None = conta_corrente



#--------------------------------------------------------------------------------------------



class Conta(ABC):
    def __init__(self, cpf):
        self.cpf = cpf
        if not fullmatch(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            raise ValueError('CPF inválido.')

    def sacar(self, valor:float) -> bool:
        if self._sacar(valor):
            return True
        else:
            return False

    def depositar(self, valor:float) -> bool:
        if self._depositar(valor):
            return True
        else:
            return False

    @abstractmethod
    def _sacar(self, valor:float) -> bool:
        pass

    @abstractmethod
    def _depositar(self, valor:float) -> bool:
        pass



class ContaCorrente(Conta):
    def __init__(self, cpf:str):
        super().__init__(cpf)

    def _sacar(self, valor:float) -> bool:
        with open(Path(__file__).parent / 'santander.json', 'r', encoding='utf_8') as santander_cliente_db:
            clientes = json.load(santander_cliente_db)
        for cliente in clientes:
            if cliente.get(self.cpf):
                if cliente[self.cpf]['saldo_corrente'] - valor >= 0:
                    cliente[self.cpf]['saldo_corrente'] -= valor
                    saque_exito = True
                else:
                    if cliente[self.cpf]['saldo_corrente'] - valor < -1000:
                        saque_exito = False
                    else:
                        cliente[self.cpf]['saldo_corrente'] -= valor
                        saque_exito = True
                break
        with open(Path(__file__).parent / 'santander.json', 'w', encoding='utf_8') as santander_cliente_db:
            json.dump(clientes, santander_cliente_db, ensure_ascii=False, indent=2)
        return saque_exito

    def _depositar(self, valor:float) -> bool:
        with open(Path(__file__).parent / 'santander.json', 'r', encoding='utf_8') as santander_cliente_db:
            clientes = json.load(santander_cliente_db)
        for cliente in clientes:
            if cliente.get(self.cpf):
                cliente[self.cpf]['saldo_corrente'] += valor
                deposito_exito = True
                break
        with open(Path(__file__).parent / 'santander.json', 'w', encoding='utf_8') as santander_cliente_db:
            json.dump(clientes, santander_cliente_db, ensure_ascii=False, indent=2)
        return deposito_exito



class ContaPoupanca(Conta):
    def __init__(self, cpf:str):
        super().__init__(cpf)

    def _sacar(self, valor:float) -> bool:
        with open(Path(__file__).parent / 'santander.json', 'r', encoding='utf_8') as santander_cliente_db:
            clientes = json.load(santander_cliente_db)
        for cliente in clientes:
            if cliente.get(self.cpf):
                if cliente[self.cpf]['saldo_poupanca'] - valor >= 0:
                    cliente[self.cpf]['saldo_poupanca'] -= valor
                    cliente[self.cpf]['saldo_corrente'] += valor
                    saque_exito = True
                else:
                    saque_exito = False
                break
        with open(Path(__file__).parent / 'santander.json', 'w', encoding='utf_8') as santander_cliente_db:
            json.dump(clientes, santander_cliente_db, ensure_ascii=False, indent=2)
        return saque_exito

    def _depositar(self, valor:float) -> bool:
        with open(Path(__file__).parent / 'santander.json', 'r', encoding='utf_8') as santander_cliente_db:
            clientes = json.load(santander_cliente_db)
        for cliente in clientes:
            if cliente.get(self.cpf):
                if cliente[self.cpf]['saldo_corrente'] - valor >= 0:
                    cliente[self.cpf]['saldo_poupanca'] += valor
                    cliente[self.cpf]['saldo_corrente'] -= valor
                    deposito_exito = True
                else:
                    if cliente[self.cpf]['saldo_corrente'] - valor < -1000:
                        deposito_exito = False
                    else:
                        cliente[self.cpf]['saldo_poupanca'] += valor
                        cliente[self.cpf]['saldo_corrente'] -= valor
                        deposito_exito = True
                break
        with open(Path(__file__).parent / 'santander.json', 'w', encoding='utf_8') as santander_cliente_db:
            json.dump(clientes, santander_cliente_db, ensure_ascii=False, indent=2)
        return deposito_exito