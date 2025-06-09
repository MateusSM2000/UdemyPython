#simple factory
#outro jeito de fazer mas dessa forma carro é uma instancia de VeiculoFactory

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

class VeiculoFactory:
    def __init__(self, tipo: str):
        self.veiculo = VeiculoFactory.criar_instancia(tipo)

    @staticmethod
    def criar_instancia(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        elif tipo == 'popular':
            return CarroPopular()
        else:
            raise ValueError("'luxo' | 'popular'")

    def buscar_cliente(self) -> None:
        self.veiculo.buscar_cliente()

carros_disponiveis = ['luxo', 'popular']
for i in range(10):
    carro = VeiculoFactory(choice(carros_disponiveis))
    carro.buscar_cliente()
print(carro)