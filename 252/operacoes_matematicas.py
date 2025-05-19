"""Classes de operações matemáticas

Este módulo contém classes para realizar operações matemáticas entre variáveis.
"""


class OperacoesMatematicasComuns:
    """Esta classe executa as operações matemáticas mais comuns

    Possui os método soma e dividir
    """
    @staticmethod
    def soma(*nums:int | float) -> int | float:
        """
        Realiza soma entre vários números
        :param nums: números a se somar
        :return: o resultado da soma
        """
        s = 0
        for num in nums:
            s += num
        return s

    @staticmethod
    def dividir(dividendo:int | float, divisor: int | float) -> int | float | str:
        """
        Realiza a divisão entre dois números
        :param dividendo: dividendo da divisão
        :param divisor: divisor da divisão
        :return: o quociente da divisão
        :raises ZeroDivisionError: se divisor == 0
        """
        try:
            q = dividendo/divisor
        except ZeroDivisionError:
            return 'Não se pode dividir um número por 0.'
        else:
            return q