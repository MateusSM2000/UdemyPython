#factory method

from random import choice
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo indo buscar cliente.')

class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular indo buscar cliente.')

class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo indo buscar cliente.')

class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular indo buscar o cliente.')

#--------------------------------------------------------------------------------

class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def criar_instancia(tipo: str) -> Veiculo:
        pass

class ZonaNorteVeiculoFactory(VeiculoFactory):
    veiculos_disponiveis = ['carro_luxo', 'carro_popular', 'moto_luxo', 'moto_popular']

    @staticmethod
    def criar_instancia(tipo: str) -> Veiculo:
        if tipo == 'carro_luxo':
            return CarroLuxo()
        elif tipo == 'carro_popular':
            return CarroPopular()
        elif tipo == 'moto_luxo':
            return MotoLuxo()
        elif tipo == 'moto_popular':
            return MotoPopular()
        else:
            raise ValueError("'moto_luxo' | 'moto_popular' | 'carro_luxo' | 'carro_popular'")

class ZonaSulVeiculoFactory(VeiculoFactory):
    veiculos_disponiveis = ['carro_popular', 'moto_popular']

    @staticmethod
    def criar_instancia(tipo: str) -> Veiculo:
        if tipo == 'carro_popular':
            return CarroPopular()
        elif tipo == 'moto_popular':
            return MotoPopular()
        else:
            raise ValueError("'moto_popular' | 'carro_popular'")


print('Zona Norte:')
for i in range(10):
    veiculo = ZonaNorteVeiculoFactory.criar_instancia(choice(ZonaNorteVeiculoFactory.veiculos_disponiveis))
    veiculo.buscar_cliente()
print()

print('Zona Sul:')
for i in range(10):
    veiculo = ZonaSulVeiculoFactory.criar_instancia(choice(ZonaSulVeiculoFactory.veiculos_disponiveis))
    veiculo.buscar_cliente()