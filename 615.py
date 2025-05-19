#no monostate há a criação de diferentes instancias na memória, mas msm assim os atributos são criados e alterados universalmente para tds as instancias de msm
#classe e suas filhas
class MonoState:
    __state = {'x':1, 'y':2}

    def __repr__(self):
        return f'{self.__dict__}'

    def __init__(self, z, a=None, b=None):
        self.__dict__ = self.__state
        self.z = z
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b


class A(MonoState):
    pass

a = MonoState(3, 20)
b = MonoState(4, b=30)
print(a)
print(b)
print()

a.x = 10
print(a)
print(b)
print()

c = A(100)
print(c)
print(a)
print(b)
print()
print()



#relembrando dicionario

dicionario1 = {'a':1, 'b':2}
dicionario2 = dicionario1
dicionario3 = dicionario1.copy()
print(dicionario2)
print(dicionario3)
dicionario1['a'] = 5
print(dicionario2)
print(dicionario3)