def passar_parametros(a):
    print('Adicionando parâmetros...')
    def decorador(func):
        print('Iniciando decorador...')
        def executar(*valores):
            print(a)
            return f'{func(*valores)} {a}'
        return executar
    return decorador

@passar_parametros('f')
@passar_parametros('e')
@passar_parametros('d')
@passar_parametros('c')
@passar_parametros('b')
@passar_parametros('a')
def soma(*nums):
    s = 0
    for num in nums:
        s = s + num
    return s

resultado = soma(2, 3, 6)
resultado = soma(10, 21)
print(resultado)