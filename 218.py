class Fabricante:
    fabricante_modelo_motor = []
    fabricantes = []
    def __init__(self, nome):
        self.fabricante = nome

    def adicionar_lista_fabricantes(self):
        Fabricante.fabricantes.append(self.fabricante)

    @staticmethod
    def adicionar_lista_detalhada(fabricante, carro, motor):
        dict_pronto = {}
        dict_pronto.update(fabricante)
        dict_pronto.update(carro)
        dict_pronto.update(motor)
        Fabricante.fabricante_modelo_motor.append(dict_pronto)



class Carro:
    carros = []
    def __init__(self, nome):
        self.carro = nome

    def adicionar_lista_carros(self):
        Carro.carros.append(self.carro)




class Motor:
    motores = []
    def __init__(self, nome):
        self.motor = nome

    def adicionar_lista_motores(self):
        Motor.motores.append(self.motor)




fiat = Fabricante('Fiat')
fiat.adicionar_lista_fabricantes()
uno2021 = Carro('Uno 2021')
uno2021.adicionar_lista_carros()
fiat1_4 = Motor('Fiat 1.4')
fiat1_4.adicionar_lista_motores()

volkswagen = Fabricante('Volkswagen')
volkswagen.adicionar_lista_fabricantes()
nivus = Carro('Nivus')
nivus.adicionar_lista_carros()
tgdi1_6turbo = Motor('TGDI 1.6 Turbo')
tgdi1_6turbo.adicionar_lista_motores()

mercedes_benz = Fabricante('Mercedes-Benz')
mercedes_benz.adicionar_lista_fabricantes()
amg150 = Carro('AMG 150')
amg150.adicionar_lista_carros()
amg2_0 = Motor('AMG 2.0')
amg2_0.adicionar_lista_motores()


amg160 = Carro('AMG 160')
amg160.adicionar_lista_carros()

uno2022 = Carro('Uno 2022')
uno2022.adicionar_lista_carros()

print(f'Fabricantes: {Fabricante.fabricantes}')
print(f'Modelos: {Carro.carros}')
print(f'Motores: {Motor.motores}\n')

Fabricante.adicionar_lista_detalhada(fiat.__dict__, uno2021.__dict__, fiat1_4.__dict__)
Fabricante.adicionar_lista_detalhada(fiat.__dict__, uno2022.__dict__, fiat1_4.__dict__)
Fabricante.adicionar_lista_detalhada(volkswagen.__dict__, nivus.__dict__, tgdi1_6turbo.__dict__)
Fabricante.adicionar_lista_detalhada(mercedes_benz.__dict__, amg150.__dict__, amg2_0.__dict__)
Fabricante.adicionar_lista_detalhada(mercedes_benz.__dict__, amg160.__dict__, amg2_0.__dict__)

print(*Fabricante.fabricante_modelo_motor, sep='\n')