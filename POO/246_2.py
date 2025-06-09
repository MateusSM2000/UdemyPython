class Multiplicar:
    def __init__(self, n):
        print(self, n)
        self._z = 10

    def __call__(self, funcao):
        print(funcao)
        def somar_(x, y):
            return funcao(x, y) * self._z
        return somar_

@Multiplicar(10)
def somar(x, y):
    return x + y


print(somar(2, 3))