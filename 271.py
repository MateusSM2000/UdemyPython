#namedtuple cria uma classe mas serve apenas para uso de atributos pois n conseguimos criar metodos com ele. E tbm esses atributos sao imutaveis com o namedtuple
#n podendo mudar o valor dos atributos apos a criacao da instancia

from collections import namedtuple
from typing import NamedTuple
#esses dois jeitos funcionam da msm maneira

class Carta(NamedTuple):
    valor: str = '3'
    naipe: str = '♣'

# Carta = namedtuple('Carta',['valor', 'naipe'], defaults=['3', '♣'])

as_espadas = Carta('as', '♠️')
print(as_espadas)
print(as_espadas.valor)
print(as_espadas.naipe)
print(as_espadas[1])
print(as_espadas._asdict())
print(as_espadas._fields)
print(Carta._field_defaults)
try:
    as_espadas.valor = 4
except AttributeError as erro:
    print(erro)

print()

valor_padrao = Carta()
print(valor_padrao)