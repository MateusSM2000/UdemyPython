class Animal:
    def __init__(self, nome):
        self.animal = nome

    def comer(self, alimento = 'ração'):
        return f'{self.animal} está comendo {alimento}'

    def tipo_racao(self, racao_definida):
        return f'{self.comer()} {racao_definida}'

    def tipo_carne(self, carne_definida):
        return f'{self.comer('carne')} {carne_definida}'

cachorro = Animal('cachorro')
print(cachorro.comer('carne'))
print()
print(cachorro.tipo_racao('premium'))
print()
print(cachorro.tipo_carne('bovina'))