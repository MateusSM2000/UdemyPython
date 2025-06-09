#outra maneira de fazer com q o init n execute td hr


class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__()
        return cls.__instances[cls]


class Singleton(metaclass=SingletonMeta):

    def __init__(self):
        print('init')
        self.tema = 'tema escuro'


a1 = Singleton()
a1.tema = 'tema claro'
print(a1.tema)
a2 = Singleton()
print(a1.tema)
print()

print(a1)
print(a2)
print(a1 == a2)
print()

a1.nome = 'Mateus'
print(a2.nome)