def gen1():
    print('Começou gen1')
    yield 1
    yield 2
    yield 3
    print('Terminou gen1')

def gen2():
    print('Começou gen2')
    yield from gen1()
    yield 4
    yield 5
    yield 6
    print('Terminou gen2')

def gen3(gen):
    print('Começou gen3')
    yield from gen()
    yield 7
    yield 8
    yield 9
    print('Terminou gen3')


for n in gen2():
    print(n)

print('\n\n\n')

for n in gen3(gen2):
    print(n)