#tem um parametro do decorador de dataclass q se chama frozen, e se for true, ele congela os atributos, n podendo mudar o valor dos atributos e nem criar novos atributos
#dps do init

from dataclasses import dataclass

@dataclass(frozen=True)
class A:
    a: int

    def criar_atributo(self):
        self.aa = 11

    def mudar_atributo(self):
        self.a = 2

a = A(1)
a.mudar_atributo()
print(a.aa)
