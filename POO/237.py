#repr nem sempre retorna uma string. se vc mandar printar o objeto da classe, vai aparecer no terminal oq vc escreveu pra retornar no repr. ele continua sendo um objeto
# da classe. tanto q se vc colocar ele dentro de uma lista, ele n vai aparecer entre as aspas q denotam q o objeto é uma string. o repr só retorna oq vc escreveu nele como
# um objeto da classe str se vc escrever no codigo repr(objeto) ou objeto.__repr__()

class Ponto:
    def __init__(self, x, y, z=None, /, *, d:str='2d'):  #td antes da / deve ser argumento posicional, e td dps do * deve ser posicional
        self.x = x
        self.y = y
        self.z = z
        self.d = d

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x!r}, y={self.y!r}, z={self.z!r}, d={self.d!r})'   #!r coloca entre aspas

p1 = Ponto(1, 2)
p2 = Ponto(1, 2, 3, d='3d')

print(p1)
print(p2)
print()

lista = [p1,p2]
print(lista)
print(type(p1), type(p2))
print()

lista = [p1.__repr__(), p2.__repr__()]
print(lista)
print(type(p1.__repr__()), type(p2.__repr__()))