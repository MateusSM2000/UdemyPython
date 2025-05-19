#é possível colocar @abstractmethod no @property. Tem vários jeitos de fazer isso, mas aki vou estrar montrando o mais comum

from abc import ABC, abstractmethod


class A(ABC):
    def __init__(self, name):
        self._name = name

    @property
    @abstractmethod   #@abstractmethod sempre vai logo acima
    def name(self):
        pass


class B(A):
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name



b = B('B')
print(b.name)
b.name = 'BB'
print(b.name)