# ao inves de explicitarmos com um raise avisando q o metodo _log é polimorfico no ex da aula 225, podemos fazer pelo jeito a seguir q tbm vai levantar um erro se a classe
# for instanciada, e já indica q terá metodos polimorficos. Aki está o jeito mais comum de fazer isso, usando @abstractmethod.
#se a classe ter pelo menos um @abstractmethod e herdar ABC, ela é considerada abstrata, pois justamente n devemos instancia-la para o polimorfismo funcionar
#classe abstrata nada mais é uma classe para se usar caso utilize metodos polimorficos

from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, msg):
        pass

    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({__class__.__name__})')



lp = LogPrintMixin()
lp.log_error('asdsadsda')
#l = Log()