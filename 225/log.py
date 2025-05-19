from pathlib import Path

LOG_FILE_PATH = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método _log nas subclasses.')   #isto justamente para avisar aos desenvolvedores q este metodo será polimorfico e q n devemos instanciar
                                                                                #esta classe para o polimorfismo funcionar

    def log_error(self, msg):
        self._log(f'Error: {msg}')         #metodos alinhados com herança podem ser polimorficos, como neste caso: o self._log() vai executar o metodo da classe do qual a instancia é
                                           #ou seja, se a instancia for do LogFixeMixing, ao fazer instancia._log(), o metodo executado será do LogFileMixin
    def log_success(self, msg):
        self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        with open(LOG_FILE_PATH, 'a', encoding='utf8') as log_file:
            log_file.write(f'{msg}\n')



class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({__class__.__name__})')



if __name__ == '__main__': #isto serve para q se importarem esse modulo log, essa parte n é executada pois o __name__ do módulo, ao importar, deixa de ser __main__
    lp = LogPrintMixin()
    lp.log_error('reinitializing program...')
    lp.log_success('logging in...')

    lf = LogFileMixin()
    lf.log_error('reinitializing program...')
    lf.log_success('logging in...')