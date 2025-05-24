#esse design pattern (memento) permite com q vc salve os atributos de um objeto fazendo um objeto da classe memento receber seus atributos

from __future__ import annotations

class Memento:
    def __init__(self, state: dict):
        self._state: dict
        super().__setattr__('_state', state)

    def get_state(self) -> dict:
        return self._state

    def __setattr__(self, key, value):
        raise AttributeError('Immutable class')


class ImageEditor:
    def __init__(self, name: str, width: int, height: int):
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(self.__dict__.copy())

    def restore(self, memento: Memento):
        self.__dict__ = memento.get_state()



img = ImageEditor('monkey.jpeg', 1920, 1080)
saved_img = img.save_state()
print(img.__dict__)
print(saved_img.get_state())
img.name = 'dog.jpeg'
print(img.__dict__)
img.restore(saved_img)
print(img.__dict__)