#esse padrao de projeto composite ha classes origem, no qual seus objetos tem pelo menos um atributo q recebe objetos de outras classes e assim por diante
# que pode se dividir em ramos de classes até chegar nos ultimos objetos, q pertencem a classe chamada de leaf. enquanto q os objetos intermediarios pertencem
# a classes chamadas de composite
#os metodos do objeto da classe origem podem executar os metodos dos filhos ate chegar no ultimo e de fato executar algo relevante

from __future__ import annotations
from abc import ABC, abstractmethod

class BoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, *child: BoxStructure) -> None:
        if isinstance(self, Product):
            raise TypeError("Cannot add child to a leaf class.")
        self._children.extend(child)

    def remove(self, child: BoxStructure) -> None:
        if isinstance(self, Product):
            raise TypeError("There is no child to remove from a leaf class.")
        if child in self._children:
            self._children.remove(child)


class Box(BoxStructure):
    def __init__(self, name:str):
        self.name = name
        self._children: list[BoxStructure] = []

    def print_content(self) -> None:
        for child in self._children:
            child.print_content()


    def get_price(self) -> float:
        return sum([child.get_price() for child in self._children])


class Product(BoxStructure):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(f'{self.name} price: {self.price}')

    def get_price(self) -> float:
        return self.price


#leaf
camiseta1 = Product('camiseta1', 100.99)
camiseta2 = Product('camiseta2', 90)
camiseta3 = Product('camiseta3', 80)
bone1 = Product('bone1', 39.5)
bone2 = Product('bone2', 40)


#composite
caixa_camisetas = Box('caixa de camisetas')
caixa_camisetas.add(camiseta1, camiseta2, camiseta3)
caixa_bones = Box('caixa de bones')
caixa_bones.add(bone1, bone2)
caixa_camisetas_e_bones = Box('caixa de camisetas e bones')
caixa_camisetas_e_bones.add(caixa_bones, caixa_camisetas)


caixa_camisetas.print_content()
print()

caixa_bones.print_content()
print()

print(caixa_camisetas.get_price())
print()

print(caixa_bones.get_price())
print()

caixa_camisetas_e_bones.print_content()
print()

print(caixa_camisetas_e_bones.get_price())
print()

caixa_camisetas.remove(camiseta1)
caixa_camisetas.print_content()