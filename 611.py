#abstract factory

from random import choice
from abc import ABC, abstractmethod

class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN indo buscar cliente.')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZN indo buscar cliente.')


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZN indo buscar cliente.')


class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZN indo buscar o cliente.')


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZS indo buscar cliente.')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZS indo buscar cliente.')


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZS indo buscar cliente.')


class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZS indo buscar o cliente.')


#--------------------------------------------------------------------------------


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def criar_instancia_carro_popular() -> VeiculoPopular:
        pass

    @staticmethod
    @abstractmethod
    def criar_instancia_carro_luxo() -> VeiculoLuxo:
        pass

    @staticmethod
    @abstractmethod
    def criar_instancia_moto_popular() -> VeiculoPopular:
        pass

    @staticmethod
    @abstractmethod
    def criar_instancia_moto_luxo() -> VeiculoLuxo:
        pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def criar_instancia_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def criar_instancia_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def criar_instancia_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()

    @staticmethod
    def criar_instancia_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def criar_instancia_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def criar_instancia_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def criar_instancia_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()

    @staticmethod
    def criar_instancia_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()








for instancia in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:

    instancia_moto_luxo = instancia.criar_instancia_moto_luxo()
    instancia_moto_luxo.buscar_cliente()

    instancia_moto_popular = instancia.criar_instancia_moto_popular()
    instancia_moto_popular.buscar_cliente()

    instancia_carro_luxo = instancia.criar_instancia_carro_luxo()
    instancia_carro_luxo.buscar_cliente()

    instancia_carro_popular = instancia.criar_instancia_carro_popular()
    instancia_carro_popular.buscar_cliente()

    print()