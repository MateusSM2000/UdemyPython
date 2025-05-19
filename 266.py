#tem como habilitar seu proprio init usando a dataclass caso queira
#o post_init roda logo apos o init automatico da dataclass. Se vc habilitar pra rodar seu proprio init, o post_init n roda mais

from dataclasses import dataclass

@dataclass(init=False)
class A:
    def __init__(self, a):
        self.a = a

a = A(1)
print(a.a)


@dataclass()
class B:
    b: int

    def __post_init__(self):
        print('Iniciando post_init')

b = B(2)