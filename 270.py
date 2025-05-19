#pode colocar parametros com valor padrao normalmente nas dataclasses, apenas se o valor padrao for mutável q terá q fazer algo diferente

from dataclasses import dataclass, field

@dataclass
class A:
    a: int = 1
    aa: list[int] = field(default_factory=list)

a = A()
print(a.__dict__)