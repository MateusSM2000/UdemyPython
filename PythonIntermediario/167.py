def passar_parametros(a=None, b=None):
    print('Adicionando parâmetros...')
    def decorador(func):
        print('Iniciando decorador...')
        def executar(*valores):
            print(a, b)
            return func(*valores)
        return executar
    return decorador


@passar_parametros(5, 10)
def soma(*nums):
    s = 0
    for num in nums:
        s = s + num
    return s

resultado1 = soma(2, 3, 6)
resultado2 = soma(10, 21)
print(resultado1)
print(resultado2)
