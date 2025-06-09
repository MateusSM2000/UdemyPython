#pra notificar se algum atributo muda de valor podemos fazer desse jeito se forem poucos atributos e uma notificação simples

class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        nome_antigo = self._nome
        self._nome = novo_nome
        if nome_antigo != novo_nome:
            print(f"Atributo 'nome' do objeto '{self}' alterado de '{nome_antigo}' para '{novo_nome}'")
            print(f'Nova situação: {self.__dict__}')


p1 = Pessoa('Mateus')
p1.nome = 'Gabriele'
print(p1.nome)
print()
print()


#agr se forem vários atributos e outras classes precisam saber q foi modificado para ai sim enviar a notificação,
# podemos criar um atributo apenas, q recebe um dicionario com oq seria seus atributos

from abc import ABC, abstractmethod

class Observers(ABC):
    @abstractmethod
    def send_notification(self, update) -> None: pass

class DatabaseCartorioMunicipal(Observers):
    def send_notification(self, update):
        print(f'Notification about characteristics modification {update} has been sent to {self.__class__.__name__}.')

class DatabaseReceitaFederal(Observers):
    def send_notification(self, update):
        print(f'Notification about characteristics modification {update} has been sent to {self.__class__.__name__}.')


class Pessoa2:
    def __init__(self, observers: list[DatabaseReceitaFederal | DatabaseCartorioMunicipal], **caracteristicas):
        self._caracteristicas = caracteristicas
        self.observers = observers

    @property
    def caracteristicas(self):
        return self._caracteristicas

    @caracteristicas.setter
    def caracteristicas(self, update:dict):
        caracteristicas_anterior = self._caracteristicas
        self._caracteristicas = {**caracteristicas_anterior, **update}
        if caracteristicas_anterior != self._caracteristicas:
            for observer in self.observers:
                observer.send_notification(update)


p2 = Pessoa2([DatabaseReceitaFederal(), DatabaseCartorioMunicipal()], nome='Mateus', idade=24, sexo='M', altura=1.83, peso=90)
p2.caracteristicas = {'idade':25, 'tipo_sanguineo':'O-'}