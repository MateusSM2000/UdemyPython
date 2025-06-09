#podemos usar essas classes para justamente armazenar estados de objetos

class Camera:
    def __init__(self, marca, filmando = False, fotografando = False):
        self.marca = marca
        self.filmando = filmando
        self.fotografando = fotografando

    def filmar(self):
        if self.filmando:
            print(f'{self.marca} já está filmando...')
            return
        self.filmando = True
        print(f'{self.marca} começou a filmar!')

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.marca} não está filmando...')
            return
        self.filmando = False
        print(f'{self.marca} parou de filmar!')

    def fotografar(self):
        if self.filmando:
            print(f'{self.marca} não pode fotografar pois está filmando...')
            return
        self.fotografando = True
        print(f'{self.marca} está fotografando...')
        self.fotografando = False
        print(f'{self.marca} fotografou com sucesso!')


c1 = Camera('Samsung')
c2 = Camera('Apple')

c1.parar_filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
print()
c2.parar_filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()