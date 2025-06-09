def adicionar_pessoa(nome, lista=[]):
    lista.append(nome)
    return lista

pessoa1 = adicionar_pessoa('Mateus')
print(pessoa1)
pessoa2 = adicionar_pessoa('Gabriele')
print(pessoa2)

print('\n\n')
#veja q ele n criou outra lista, ou seja, no parâmetro padrao ele n cria um novo mutável. Há um jeito de fazer criar outra lista no corpo da funcao ao inves no parametro

def adicionar_pessoas2(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

pessoa1 = adicionar_pessoas2('Mateus')
print(pessoa1)
pessoa2 = adicionar_pessoas2('Gabriele')
print(pessoa2)
print()
pessoa1.append('Schmidt Mesquita')
pessoa2.append('Borges')
print(pessoa1)
print(pessoa2)
print()
adicionar_pessoas2('dasdas', pessoa1)
adicionar_pessoas2('asdsads', pessoa2)
print(pessoa1)
print(pessoa2)