class Planeta:
    def __init__(self, nome):
        self.nome = nome
        self.galaxia = None
        self.gn = None

    @staticmethod
    def _galaxy_number(n):
        print(n)
        def galaxy_number(method):
            print(method)
            def add_number(self, special=0):
                print(self, special)
                method(self)
                if 'Milky Way' in self.galaxia:
                    self.gn = 1
                elif 'Andromeda' in self.galaxia:
                    self.gn = 2
                return self.gn + n + special
            return add_number
        return galaxy_number

    @_galaxy_number(10)
    def add_galaxy(self):
        if 'Terra' in self.nome:
            self.galaxia = 'Milky Way'
        elif 'USX-68' in self.nome:
            self.galaxia = 'Andromeda'




terra = Planeta('Terra')
usx68 = Planeta('USX-68')

print(terra.add_galaxy(1000), terra.galaxia)
print()
print(usx68.add_galaxy(), usx68.galaxia)