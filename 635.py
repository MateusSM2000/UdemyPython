#basicamente esse padrao de projeto decorator serve pra vc guardar estados de um objeto, no qual um
# objeto de outra classe recebe uma copia do objeto principal, podendo o alterar sem alterar as copias


from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from copy import deepcopy



class Ingredient(ABC):
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.5


@dataclass
class Sausage(Ingredient):
    price: float = 5.4


@dataclass
class Bacon(Ingredient):
    price: float = 2.5


@dataclass
class Egg(Ingredient):
    price: float = 7.5


@dataclass
class Cheese(Ingredient):
    price: float = 1.99


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 6.39


@dataclass
class PotatoSticks(Ingredient):
    price: float = 4.09







class Hotdog(ABC):
    _name: str
    _ingredients: list[Ingredient]
    _price: float

    @property
    def price(self) -> float:
        return round(sum([ingredient.price for ingredient in self.ingredients]), 2)

    @price.setter
    def price(self, price: float):
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def ingredients(self) -> list[Ingredient]:
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: list[Ingredient]):
        self._ingredients = ingredients

    @abstractmethod
    def add_ingredients(self, *ingredients: Ingredient) -> None: pass


class SimpleHotdog(Hotdog):
    def __init__(self, name: str):
        self._name = name
        self._ingredients: list[Ingredient] = []
        self._price: float = 0

    def add_ingredients(self, *ingredients: Ingredient) -> None:
        self._ingredients.extend(ingredients)


class SpecialHotdog(Hotdog):
    def __init__(self, name: str):
        self._name = name
        self._ingredients: list[Ingredient] = []
        self._price: float = 0

    def add_ingredients(self, *ingredients: Ingredient) -> None:
        self._ingredients.extend(ingredients)



class HotdogDecorator:
    def __init__(self, hotdog: Hotdog):
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        return round(sum([ingredient.price for ingredient in self.hotdog.ingredients]), 2)

    @price.setter
    def price(self, price: float):
        self.hotdog._price = price

    @property
    def name(self):
        return self.hotdog._name

    @name.setter
    def name(self, name: str):
        self.hotdog._name = name

    @property
    def ingredients(self) -> list[Ingredient]:
        return self.hotdog._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: list[Ingredient]):
        self.hotdog._ingredients = ingredients



simple_hotdog = SimpleHotdog('x-dog')
simple_hotdog.add_ingredients(Bread(), Sausage())
special_hotdog = SpecialHotdog('special x-dog')
special_hotdog.add_ingredients(Cheese(), Sausage(), Bread(), Sausage(), Bacon(),
                               Egg(), MashedPotatoes(), PotatoSticks())

print(simple_hotdog.price)
print(simple_hotdog._ingredients)
print(special_hotdog.price)
print(special_hotdog._ingredients)
print()

decorated_xdog = HotdogDecorator(deepcopy(simple_hotdog))
print(decorated_xdog.price)
simple_hotdog.add_ingredients(PotatoSticks())
print(decorated_xdog.ingredients)
print(simple_hotdog._ingredients)
