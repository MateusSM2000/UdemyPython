from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    try:
        file = open(path, mode)
        yield file
    except Exception as erro:
        print(erro)
        file.close()
        print('arquivo fechado')



with my_open('242.txt', 'w') as arquivo:
    arquivo.write('Linha1', 123)