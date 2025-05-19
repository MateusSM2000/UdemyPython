#simple factory

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
    @staticmethod
    def criar_instancia(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        elif tipo == 'popular':
            return CarroPopular()
        else:
            raise ValueError("'luxo' | 'popular'")


carros_disponiveis = ['luxo', 'popular']
for i in range(10):
    carro = VeiculoFactory.criar_instancia(choice(carros_disponiveis))
    carro.buscar_cliente()
print(carro)