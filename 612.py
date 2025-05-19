#singleton faz com q haja apenas uma instancia na memoria

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

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