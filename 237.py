#repr altera oq o print da instancia retorna. Usado para informar desenvolvedores

class Ponto:
    def __init__(self, x, y, z=None, /, *, d:str='2d'):  #td antes da / deve ser argumento posicional, e td dps do * deve ser posicional
        self.x = x
        self.y = y
        self.z = z
        self.d = d

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x!r}, y={self.y!r}, z={self.z!r}, d={self.d!r})'   #!r coloca entre aspas se for string

p1 = Ponto(1, 2)
p2 = Ponto(1, 2, 3, d='3d')

print(p1)
print(p2)