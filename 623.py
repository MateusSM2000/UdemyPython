#dessa maneira vc consegue fazer com q se um metodo de uma classe n consegue tratar os valores, vc passa pra metodos de outras classes em sequencia, ate algum conseguir
# tratar, ou levantar um erro se n tratar, como quiser

from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def _handle(self, value): pass

    @staticmethod
    def handle(value):
        HandleABC()._handle(value)


class HandleABC(Handler):
    def __init__(self):
        self.sucessor_instance: Handler = HandleDEF()

    def _handle(self, value):
        if value in ['A','B','C']:
            print(f'Method from {self.__class__.__name__} has handled value {value}')
        else:
            self.sucessor_instance._handle(value)


class HandleDEF(Handler):
    def __init__(self):
        self.sucessor_instance = HandleUnidentified()

    def _handle(self, value):
        if value in ['D','E','F']:
            print(f'Method from {self.__class__.__name__} has handled value {value}')
        else:
            self.sucessor_instance._handle(value)


class HandleUnidentified(Handler):
    def _handle(self, value):
        raise ValueError(f'No method from the classes could handle value {value}')



Handler.handle('A')
Handler.handle('B')
Handler.handle('C')
Handler.handle('D')
Handler.handle('E')
Handler.handle('F')
Handler.handle('G')