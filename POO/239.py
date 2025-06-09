# new é executado antes do init

class A:
    def __new__(cls, *args, **kwargs):
        print('INICIO NEW')
        print(cls)
        print(args)
        print(kwargs)
        instancia = super().__new__(cls)
        instancia.a = 'a'
        print('FIM NEW')
        print()
        return instancia

    def __init__(self, aa):
        print('INICIO INIT')
        self.aa = aa
        print('FIM INIT')
        print()


a = A('aa')
print(a.__dict__)