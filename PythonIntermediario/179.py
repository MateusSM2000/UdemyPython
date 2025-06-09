def funcao_recursiva(inicio = 0, fim = 10):
    print(inicio, fim)
    if inicio >= 10:
        return inicio
    inicio = inicio + 1
    return funcao_recursiva(inicio, fim)

print(funcao_recursiva())


def fatorial(n, fat = 1):
    fat = fat * n
    if n == 1:
        return fat
    n = n - 1
    return fatorial(n, fat)

print('\n')
print(fatorial(5))