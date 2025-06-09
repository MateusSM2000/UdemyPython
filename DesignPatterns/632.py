#esse padrao de projeto flyweight faz um cache dos objetos de uma classe cujos valores dos atributos n costumam mudar com frequencia
#dessa forma, ele verifica se os valores do atributos do objeto já existem no dicionario. se sim, ele retorna o objeto no cache, se não, ele cria um novo objeto

from __future__ import annotations

class Client:
    _address_flyweight: AddressFlyweight

    def __init__(self, name: str, street: str, address_number: str, zip_code: str):
        self.name = name
        self._street = street
        self._address_number = address_number
        self._zip_code = zip_code

    def add_address(self, address: AddressFlyweight) -> None:
        self._address_flyweight = address

    def list_addresses(self) -> None:
        self._address_flyweight.print_address(self._street, self._address_number, self._zip_code)


class AddressFlyweight:
    def __init__(self, neighborhood: str, city: str, state: str):
        self._neighborhood = neighborhood
        self._city = city
        self._state = state

    def print_address(self, street: str, address_number: str, zip_code: str) -> None:
        print(f'{street}, {address_number} - {self._city}/{self._state}, {self._neighborhood}, {zip_code}')


class AddressFactory:
    _addresses: dict = {}

    @staticmethod
    def _get_key(**kwargs: str) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs: str) -> AddressFlyweight:
        key = self._get_key(**kwargs)
        print(self._addresses)

        try:
            address_flyweight = self._addresses[key]
            print('usando objeto já criado')
        except KeyError:
            address_flyweight = AddressFlyweight(**kwargs)
            print('criando novo objeto')
            self._addresses[key] = address_flyweight
        return address_flyweight



address_factory = AddressFactory()
a1 = address_factory.get_address(neighborhood='Centro', city='São Paulo', state='SP')
a2 = address_factory.get_address(neighborhood='Centro', city='São Paulo', state='SP')
print()

c1 = Client('Mateus', 'Rua 1', '100', '98765-432')
c1.add_address(a1)
c1.list_addresses()
print()

c2 = Client('Gabriele', 'Rua boa morte', '100', '12345-678')
c2.add_address(a1)
c2.list_addresses()