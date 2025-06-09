#o init ser executado td hr pode ser um problema, no qual pode ser resolvido dessa maneira


def singleton(classe):
    __instances = {}
    def singleton_():
        if classe not in __instances:
            __instances[classe] = classe()
        return __instances[classe]
    return singleton_


@singleton
class Singleton:

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