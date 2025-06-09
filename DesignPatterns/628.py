from abc import ABC, abstractmethod

class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass


class Control(IControl):
    def top(self) -> None:
        print('Moving up.')

    def down(self) -> None:
        print('Moving down.')

    def right(self) -> None:
        print('Moving right.')

    def left(self) -> None:
        print('Moving left.')


class NewControl:
    @staticmethod
    def move_top() -> None:
        print('Moving up.')

    @staticmethod
    def move_down() -> None:
        print('Moving down.')

    @staticmethod
    def move_right() -> None:
        print('Moving right.')

    @staticmethod
    def move_left() -> None:
        print('Moving left.')



class ControlAdapter:
    def __init__(self):
        self.new_control = NewControl()

    def top(self) -> None:
        self.new_control.move_top()

    def down(self) -> None:
        self.new_control.move_down()

    def right(self) -> None:
        self.new_control.move_right()

    def left(self) -> None:
        self.new_control.move_left()


c = Control()

c.top()
c.down()
c.right()
c.left()
print()

#se tivesse q mudar td codigo pra nova classe de controle só iria ter q mudar o objeto e o codigo funciona do msm jeito

c = ControlAdapter()

c.top()
c.down()
c.right()
c.left()