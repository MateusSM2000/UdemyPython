from log import LogFileMixin

class Eletronico:
    def __init__(self):
        self._ligado = False

    def ligar(self):
        self._ligado = True


    def desligar(self):
        self._ligado = False



class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__()
        self.smartphone = nome

    def ligar(self):
        lf = LogFileMixin()
        if not self._ligado:
            super().ligar()
            lf.log_success(f'{self.smartphone} ligado com sucesso!!')
        else:
            lf.log_error(f"{self.smartphone} não executou 'ligar' pois já está ligado.")

    def desligar(self):
        lf = LogFileMixin()
        if self._ligado:
            super().desligar()
            lf.log_success(f'{self.smartphone} desligado com sucesso!!')
        else:
            lf.log_error(f"{self.smartphone} não executou 'desligar' pois já está desligado.")