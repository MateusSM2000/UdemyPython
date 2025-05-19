#os objetos selfs (modelo, ano (chamados de atributos)) do escopo do init podem ser acessados nos métodos

class Carro:
    def __init__(self,modelo,ano):
        self.modelo = modelo
        self.ano = ano
    def acelerar(self):
        print(f'{self.modelo} {self.ano} está celerandooo vruuuuuum!!')
    def frear(self):
        print(f'{self.modelo} {self.ano} está freandooooooo fudeuuuuu!!')

lamborghini = Carro('aventador', 2022)
porsche = Carro('911spyder', 2025)

print(lamborghini.modelo)
print(lamborghini.ano)
lamborghini.acelerar()
lamborghini.frear()
print()

print(porsche.modelo)
print(porsche.ano)
porsche.acelerar()
porsche.frear()