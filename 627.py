#esse design pattern (memento) permite q vc salve os atributos de um objeto, podendo voltar esse objeto a estados anteriores

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

    def __repr__(self):
        return f'{self.__dict__}'


class Caretaker:
    def __init__(self, originator: ImageEditor):
        self._originator = originator
        self._mementos: list[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())



img = ImageEditor('monkey.jpeg', 1920, 1080)
print(img)
caretaker = Caretaker(img)
caretaker.backup()

img.name = 'lion.jpeg'
print(img)
caretaker.backup()

img.name = 'fish.jpeg'
print(img)
caretaker.backup()

caretaker.restore()
print(img)

caretaker.restore()
print(img)

caretaker.restore()
print(img)
caretaker.restore()
print(img)
caretaker.restore()
print(img)
caretaker.restore()
print(img)