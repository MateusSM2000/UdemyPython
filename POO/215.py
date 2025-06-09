class Escritor:
    def __init__(self):
        self.ferramenta = None

class FerramentaDeEscrever:
    def __init__(self,nome):
        self.ferramenta = nome

    def escrever(self):
        print(f'{self.ferramenta} está escrevendo.')


Mateus = Escritor()
caneta = FerramentaDeEscrever('Caneta')

caneta.escrever()

Mateus.ferramenta = caneta
Mateus.ferramenta.escrever()