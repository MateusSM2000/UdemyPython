#esse padrao de projeto proxy eh mt versátil, é uma classe q imita outra, podendo executar ou adiar funções e guardar informações do objeto da classe original
#nessa aula ele foi utilizado pra servir como se fosse um cache, guardando o return da função q simula uma requisição com um tempo de espera
#apos executar a função de requisição uma vez, n há mais esperas ao executar a função do proxy novamente

from time import sleep
from abc import ABC, abstractmethod

class IUser(ABC):
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> list[dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> dict: pass


class User(IUser):
    def __init__(self, first_name: str, last_name: str):
        sleep(2) #simulando requisição
        self.firstname = first_name
        self.lastname = last_name

    def get_addresses(self) -> list[dict]:
        sleep(2) #simulando requisição
        return [
            {'street': 'Av. Brasil', 'number': 1234},
        ]

    def get_all_user_data(self) -> dict:
        sleep(2) #simulando requisição
        return {
            'cpf': '111.111.111-11',
            'rg': '111111111'
        }


class UserProxy(IUser):
    def __init__(self, first_name: str, last_name: str):
        self.firstname = first_name
        self.lastname = last_name
        self._real_user: User
        self._cached_addresses: list[dict]
        self._cached_all_user_data: dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = User(self.firstname, self.lastname)

    def get_addresses(self) -> list[dict]:
        self.get_real_user()
        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()
            return self._cached_addresses
        return self._cached_addresses


    def get_all_user_data(self) -> dict:
        self.get_real_user()
        if not hasattr(self, '_cached_all_user_data'):
            self._cached_all_user_data = self._real_user.get_all_user_data()
            return self._cached_all_user_data
        return self._cached_all_user_data


mateus = UserProxy('Mateus', 'Ferreira')

print(mateus.firstname)
print(mateus.lastname)
#ate aki eh executado sem pausas

print(mateus.get_addresses())
print(mateus.get_all_user_data())
#ate aki eh executado em 6 segundos
#mas a partir daki n ha mais pausas pois a funcao q simula a requisição n sera mais executada

print(mateus.get_addresses())
print(mateus.get_all_user_data())

print(mateus.get_addresses())
print(mateus.get_all_user_data())

print(mateus.get_addresses())
print(mateus.get_all_user_data())