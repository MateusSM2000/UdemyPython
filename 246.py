class Multiplicar:
    def __init__(self, funcao):
        print(self, funcao)
        self.funcao = funcao     #no caso de classes o init já funciona como uma funcao externa q impede q a funcao @ seja chamada infinitas vezes
        self._z = 10

    def __call__(self, x, y):
        return self.funcao(x,y) * self._z

@Multiplicar
def somar(x, y):
    return x + y


print(somar(2, 3))