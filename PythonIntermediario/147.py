#generator é como se fosse uma lista/tupla só q os elementos dela n sao armazenados por completo. O generator sempre tera menos bytes q uma lista/tupla. Só q no generator n tem como
#acessar os indices e nem seu tamanho com len, apenas com a funçao next(generator) vc consegue acessar sequencialmente do inicio ao fim elemento por elemento
from sys import getsizeof

generator = (n for n in range(1000000))
lista = [n for n in range(1000000)]
print(getsizeof(generator))
print(getsizeof(lista))
print(generator)


print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print('\n\n')


#agr o yield em uma função é como se fosse um generator, vc dá next na função e ela executa até o próximo yield. Basicamente um return com pausas
def funcaogenerator1():
    print('a')
    yield 1
    print('b')
    yield 2
    print('c')
    yield 3
    print('d')
    #return 4

x = funcaogenerator1()
print(x)
print(next(x))
#print(next(x))
#print(next(x))
#print(next(x))
print('\n\n\n')

for n in x:
    print(n)
print('\n\n\n')



def funcaogenerator2(n=0, maximo=20):
    while True:
        yield n
        n = n +1
        if n > maximo:
            return

for a in funcaogenerator2():
    print(a)
