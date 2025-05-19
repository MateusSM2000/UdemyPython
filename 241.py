class MyOpen:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self._arquivo = None

    def __enter__(self):
        self._arquivo = open(self.path, self.mode, encoding='utf8')
        return self._arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):     #esses parametros sao de exceção
        self._arquivo.close()
        print(exc_type)
        print(exc_val)
        print(exc_tb)


with MyOpen('240.txt', 'w') as arquivo:
    arquivo.write('a', 132)