# Exercício - Adiando execução de funções
def definir_soma(x):
    def soma(y):
        return x + y
    return soma


def definir_multiplicador(x):
    def multiplica(y):
        return x * y
    return multiplica



soma_com_cinco = definir_soma(5)
multiplica_por_dez = definir_multiplicador(10)

print(multiplica_por_dez(20))
print(soma_com_cinco(30))