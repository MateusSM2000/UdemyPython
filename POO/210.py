#@staticmethod nada mais é doq um função qql q simplesmente está dentro de uma classe mas n aceita self nem cls. Uma função normal

class OperacoesMatematicas:
    @staticmethod
    def somar(*nums):
        s = 0
        for num in nums:
            s += num
        return s

    @staticmethod
    def dividir(dividendo, divisor):
        try:
            return dividendo / divisor
        except ZeroDivisionError:
            return 'Não é possível dividir por 0.'



print(OperacoesMatematicas.somar(1, 2, 3))
print(OperacoesMatematicas.dividir(4,2))