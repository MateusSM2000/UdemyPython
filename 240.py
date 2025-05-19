# os metodos __enter__ e __exit__ sao executados nessa ordem ao escrever 'with nome_classe():'. E oq tá escrito indentando no with é executado entre enter e exit
# o return do __enter__ vai para o objeto 'with nome_classe() as objeto:'

class MyOpen:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self._arquivo = None

    def __enter__(self):
        self._arquivo = open(self.path, self.mode, encoding='utf8')
        return self._arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._arquivo.close()


with MyOpen('240.txt', 'w') as arquivo:
    arquivo.write('a')