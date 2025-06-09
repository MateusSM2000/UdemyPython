#basicamente a metaclasse é utilizada em mts poucos casos, quando vc quer executar códigos durante a propria criação de classes e instancias

def meu_repr(self):
    return f'{self.__dict__}'

class Meta(type):
    def __new__(mcs, name, bases, dct):  #cria a classe, SEMPRE será executado
        print('INICIO NEW METACLASSE')
        print(mcs)
        print(name)
        print(bases)
        print(dct)
        cls = super().__new__(mcs, name, bases, dct)
        print(cls)
        cls.atributo = 'qualquer coisa'
        cls.__repr__ = meu_repr
        print(cls.__dict__)

        if 'atributo' not in cls.__dict__:
            raise NotImplementedError(f"Atributo 'atributo' da classe {cls} não definido.")

        try:
            if not callable(cls.__dict__['falar']):
                raise NotImplementedError(f"Método 'falar' da classe {cls} não implementado.")
        except KeyError:
            raise NotImplementedError(f"Método 'falar' da classe {cls} não implementado.")

        print('FIM NEW METACLASSE')
        print()
        return cls


    def __call__(cls, *args, **kwargs):     #cria as instancias da classe. Init e new da classe sao executados dentro dele
        print('INICIO CALL METACLASSE')
        print(cls)
        print(args)
        print(kwargs)
        instancia = super().__call__(*args, **kwargs)
        print(instancia)
        if 'cidadania' not in instancia.__dict__:
            raise NotImplementedError(f"Atributo 'cidadania' da instância {instancia} não definido.")
        print('FIM CALL METACLASSE')
        print()
        return instancia


class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('INICIO NEW PESSOA')
        instancia = super().__new__(cls)
        print('FIM NEW PESSOA')
        print()
        return instancia


    def __init__(self, nome, sobrenome, cidadania='brasileiro'):
        print('INICO INIT PESSOA')
        self.nome = nome
        self.sobrenome = sobrenome
        self.cidadania = cidadania
        print('FIM INIT PESSOA')
        print()

    def falar(self):
        print(f'{self.nome} está falando.')



p1 = Pessoa('Mateus', 'Schmidt Mesquita')
p2 = Pessoa('Gabriele', 'Borges')
p3 = Pessoa('Marcia Regina', 'Schmidt Mesquita')