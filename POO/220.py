#earnings call é uma subclasse de empresa. Ela herda todos atributos e metodos da superclasse(classe mãe)

class Empresa:
    def __init__(self,nome, *departamentos):
        self.nome = nome
        self.departamentos = departamentos

    def release_earnings_call(self):
        print(f"{self.nome}'s {self.departamentos[1]} department has released its earnings call to the public.")


class EarningsCall(Empresa):
    #calculates earnings...
    ...



nvidia = EarningsCall('Nvidia', 'RH','Financeiro','Engenharia')
print(nvidia.nome, nvidia.departamentos)
nvidia.release_earnings_call()
